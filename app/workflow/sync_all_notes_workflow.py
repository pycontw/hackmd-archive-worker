"""
Implementation of the workflow for syncing all notes
"""
import os
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

import requests
from config import config
from handler.markdown_handler import get_metadata
from handler.meilisearch_handler import MeilisearchHandler
from loguru import logger
from workflow.base import BaseWorkflow


@dataclass
class OrgDirConfig:
    name: str
    path: str
    subdirs: Optional[Dict[str, Dict]] = None


class SyncAllNotesWorkflow(BaseWorkflow):
    """
    Workflow to sync all notes
    """

    def __init__(self, configuration_path: Path):
        super().__init__(configuration_path)
        self.meilisearch_handler = MeilisearchHandler()

    def download_notes(self):
        """Download notes from HackMD"""
        logger.info("Start to download notes from HackMD")
        if not config.HACKMD_COOKIE or not config.HACKMD_URL:
            logger.error("HackMD cookie or URL is not configured")
            raise Exception("HackMD cookie or URL is not configured")
        resp = requests.get(
            config.HACKMD_URL, cookies={"connect.sid": config.HACKMD_COOKIE}
        )
        logger.info("Response status code: {}", resp.status_code)
        with tempfile.NamedTemporaryFile("wb") as tmp:
            tmp.write(resp.content)
            shutil.unpack_archive(tmp.name, self.output_path, "zip")
        logger.info("Stored notes at {}", self.output_path)
        logger.info("Downloading notes from HackMD successfully")

    def classify_notes(self):
        """Classify notes into correct folder position"""
        dir_settings = self.directory_hierarchy_setting["classify_dirs"]
        default_dir = self.directory_hierarchy_setting["unsorted_dir"]
        team_to_path = {}
        org_to_path = {}
        for organization in dir_settings:
            organization_dir = OrgDirConfig(
                name=organization,
                path=dir_settings[organization]["path"],
                subdirs=dir_settings[organization]["subdirs"],
            )
            os.makedirs(organization_dir.path, exist_ok=True)
            if organization_dir.subdirs:
                for team_dir in organization_dir.subdirs:
                    team_dir_config = OrgDirConfig(
                        name=team_dir,
                        path=f'{organization_dir.path}/{organization_dir.subdirs[team_dir]["dirname"]}',
                    )
                    os.makedirs(team_dir_config.path, exist_ok=True)
                    team_to_path[frozenset([team_dir])] = team_dir_config.path
            org_to_path[frozenset([organization])] = organization_dir.path
        os.makedirs(default_dir, exist_ok=True)

        # Find out all *.md
        for filepath in list(Path().glob(f"{self.output_path}/*.md")):
            with open(filepath, "r") as f:
                content = f.read()
            metadata = get_metadata(content)
            file_tags = frozenset(
                metadata["tags"][0].strip().split(", ")
                if "tags" in metadata
                else frozenset()
            )

            # transform to set and sort to correct directory
            tags_checking_order = [*team_to_path.items(), *org_to_path.items()]
            for tag_set, tag_path in tags_checking_order:
                if tag_set.issubset(file_tags):
                    os.rename(filepath, f"{tag_path}/{filepath.name}")
                    break
            else:
                # Move to default folder
                os.rename(filepath, f"{default_dir}/{filepath.name}")

    def build_index(self):
        """Build index for archived notes"""
        self.meilisearch_handler.create_index("hackmd")

    def index_notes(self):
        """Index the notes into Meilisearch"""
        self.meilisearch_handler.index_notes(f"{self.output_path}/*.md", "hackmd")

    def execute_hackmd_index(self):
        """Execute hackmd indexing workflow"""
        self.build_index()
        self.index_notes()

    def execute(self, enable_index: bool = False):
        """
        Execute sync all notes workflow
        """
        logger.info("Executing {}", self.__class__.__name__)
        self.download_notes()
        self.classify_notes()
        if enable_index:
            self.build_index()
