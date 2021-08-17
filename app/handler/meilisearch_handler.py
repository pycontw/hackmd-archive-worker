"""
Handler for handling meilisearch operations
"""

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
