"""
Handler for handling meilisearch operations
"""
import os
import glob
from hashlib import sha256

from dataclasses import dataclass
from typing import Optional

import meilisearch
from meilisearch.index import Index

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

    def index_notes(self, index_name: str):
        documents = []
        index = self.client.index(index_name)
        filepaths = glob.glob("build/*.md", recursive=True)
        for filepath in filepaths:
            filename = os.path.basename(filepath)
            hash = sha256()
            hash.update(filepath.encode())
            with open(filepath, "r") as open_file:
                documents.append({
                    "id": hash.hexdigest(),
                    "tags": [],
                    # discard '.md' suffix
                    "title": filename[:-3],
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
