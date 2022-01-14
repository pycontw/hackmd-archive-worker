"""
Implementation of the workflow for syncing all notes
"""
from pathlib import Path

from handler.meilisearch_handler import MeilisearchHandler
from workflow.base import BaseWorkflow


class SyncAllNotesWorkflow(BaseWorkflow):
    """
    Workflow to sync all notes
    """
    def __init__(self, setting_path: Path):
        super().__init__(setting_path)
        self.meilisearch_handler = MeilisearchHandler()

    def download_notes(self):
        """Download notes"""
        handler = MeilisearchHandler()
        self.load_output_setting()
        handler.download_notes(self.output_path)

    def classify_notes(self):
        """Classify notes into correct folder position"""

    def upload(self):
        """Upload notes to the GitHub Repository"""

    def build_index(self):
        """Build index for archived notes"""
        self.meilisearch_handler.create_index("hackmd")

    def index_notes(self):
        """Index the notes into Meilisearch"""
        self.meilisearch_handler.index_notes(f"{self.output_path}/*.md", "hackmd")

    def execute_hackmd_index(self):
        """Execute hackmd indexing workflow"""
        self.load_output_setting()
        self.build_index()
        self.index_notes()
