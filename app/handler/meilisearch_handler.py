"""
Handler for handling meilisearch operations
"""
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Optional

from config import config
from meilisearch.client import Client as MeilisearchClient
from meilisearch.index import Index


@dataclass
class MeilisearchHandler:
    """
    Class for handling meilisearch operations
    """

    meilisearch_url: str = config.MEILISEARCH_URL
    master_key: Optional[str] = config.MEILISEARCH_MASTER_KEY

    def __post_init__(self):
        self.client = MeilisearchClient(self.meilisearch_url, self.master_key)

    def create_index(self, index_name: str) -> Index:
        """Invoke client to create index"""
        return self.client.index(uid=index_name)

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
                documents.append(
                    {
                        "id": hash_.hexdigest(),
                        "tags": [],  # TODO: Add tags information
                        "title": filepath.stem,
                        "content": open_file.read()
                        # TODO: Add url link
                    }
                )
        index.add_documents(documents)
        # TODO Check if all documents is added
        index.update_settings({"searchableAttributes": ["title", "content"]})
        # Only display title
        # Displaying content is not readable and has large performance impact after testing
        index.update_settings({"displayedAttributes": ["title"]})
