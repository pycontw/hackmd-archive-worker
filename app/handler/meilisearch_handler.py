"""
Handler for handling meilisearch operations
"""
import tempfile
from pathlib import Path
from hashlib import sha256

from dataclasses import dataclass
from typing import Optional

import shutil
from loguru import logger
import requests
import meilisearch
from meilisearch.index import Index
import yaml

from config import config


@dataclass
class MeilisearchHandler:
    """
    Class for handling meilisearch operations
    """

    host: Optional[str] = config.MEILISEARCH_HOST
    port: Optional[int] = config.MEILISEARCH_PORT
    master_key: Optional[str] = None

    def __post_init__(self):
        self.meilisearch_url = f"{self.host}:{self.port}"
        self.client = meilisearch.Client(self.meilisearch_url, self.master_key)

    def create_index(self, index_name: str) -> Index:
        """Invoke client to create index"""
        return self.client.index(uid=index_name)

    def download_notes(self, yaml_path: str):
        yaml_config: dict = {}
        with open(yaml_path, "r") as stream:
            yaml_config = yaml.safe_load(stream)
        resp = requests.get(
            config.HACKMD_URL,
            cookies={"connect.sid": config.HACKMD_COOKIE}
        )
        with tempfile.NamedTemporaryFile('wb') as tmp:
            tmp.write(resp.content)
            shutil.unpack_archive(tmp.name, yaml_config["output_dir"], "zip")

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
            hash = sha256()
            hash.update(str(filepath).encode())
            with open(filepath, "r") as open_file:
                documents.append({
                    "id": hash.hexdigest(),
                    "tags": [],
                    "title": filepath.stem,
                    "content": open_file.read()
                })
        index.add_documents(documents)
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
