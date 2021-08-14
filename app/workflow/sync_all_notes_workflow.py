"""
Implementation of the workflow for syncing all notes
"""

from workflow.base import BaseWorkflow


class SyncAllNotesWorkflow(BaseWorkflow):
    """
    Workflow to sync all notes
    """

    def download_notes(self):
        """Download notes"""

    def classify_notes(self):
        """Classify notes into correct folder position"""

    def upload(self):
        """Upload notes to the GitHub Repository"""
