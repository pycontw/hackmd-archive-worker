"""
Handler for handling meilisearch operations
"""
import tempfile
import os
from pathlib import Path
from hashlib import sha256

from dataclasses import dataclass
from typing import Optional, Dict, Union

import shutil
import requests
from meilisearch.client import Client as MeilisearchClient
from meilisearch.index import Index

from config import config


@dataclass
class MeilisearchHandler:
    """
    Class for handling meilisearch operations
    """

    host: Optional[str] = config.MEILISEARCH_HOST
    port: Optional[int] = config.MEILISEARCH_PORT
    master_key: Optional[str] = config.MEILISEARCH_MASTER_KEY

    def __post_init__(self):
        self.meilisearch_url = f"{self.host}:{self.port}"
        self.client = MeilisearchClient(self.meilisearch_url, self.master_key)

    def create_index(self, index_name: str) -> Index:
        """Invoke client to create index"""
        return self.client.index(uid=index_name)

    def download_notes(self, output_path: str):
        """Download notess from Hackmd"""
        resp = requests.get(
            config.HACKMD_URL,
            cookies={"connect.sid": config.HACKMD_COOKIE}
        )
        with tempfile.NamedTemporaryFile('wb') as tmp:
            tmp.write(resp.content)
            shutil.unpack_archive(tmp.name, output_path, "zip")

    def index_notes(self, parse_path: str, index_name: str):
        """
            Indexing notes to Meilisearch

            Parameters:
                parse_path: Note storage path for glob parsing
                index_name: Index for document storage
        """
        documents = []
        index = self.client.index(index_name)
        for filepath in list(Path().glob(parse_path)):
            hash_ = sha256()
            hash_.update(str(filepath).encode())
            with open(filepath, "r") as open_file:
                documents.append({
                    "id": hash_.hexdigest(),
                    "tags": [], #TODO: Add tags information
                    "title": filepath.stem,
                    "content": open_file.read()
                    #TODO: Add url link
                })
        index.add_documents(documents)
        #TODO Check if all documents is added
        index.update_settings({
            "searchableAttributes": [
                "title",
                "content"
            ]
        })
        # Only display title
        # Displaying content is not readable and has large performance impact after testing
        index.update_settings({
            "displayedAttributes": [
                "title"
            ]
        })

    def classify_notes(self, output_dir: str, dir_settings: Dict[str, Union[str, Dict]], default_dir: str):
        """Classify Hackmd notes to related directories

            Parameters:
                output_dir: Hackmd notes output directory
                dir_settings: Directory settings to construct directories
                default_dir: Default directory for notes that can't be classified
        """
        # Construct directories and dictionary mapping
        tag_mapping = {}
        for dir_name, dir_setting in dir_settings.items():
            os.makedirs(dir_setting["path"], exist_ok=True)
            for subdir_name, subdir_setting in dir_setting["subdirs"].items():
                os.makedirs(
                    f"{dir_setting['path']}/{subdir_setting['path']}",
                    exist_ok=True
                )
                tag_mapping[
                    frozenset([dir_name, subdir_name])
                ] = f"{dir_setting['path']}/{subdir_setting['path']}"
        os.makedirs(default_dir, exist_ok=True)

        # Find out all *.md
        for filepath in list(Path().glob(f"{output_dir}/*.md")):

            # TODO: get tag from markdown
            file_tags = frozenset([])
            # transform to set and sort to correct directory
            for tag_set, tag_path in tag_mapping.keys():
                if tag_set.is_subset(file_tags):
                    os.rename(filepath, f"{tag_path}/{filepath.name}")
                    continue
            # Move to default folder
            os.rename(filepath, f"{default_dir}/{filepath.name}")
