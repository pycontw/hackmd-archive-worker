"""Main module for running app"""
from enum import Enum

import typer
from config import Settings
from loguru import logger
from workflow.sync_all_notes_workflow import SyncAllNotesWorkflow


def sync_all_hackmd_notes_to_github():
    """Sync all hackmd notes to github"""
    settings = Settings()
    logger.info("Start to sync all hackmd notes to github")
    logger.debug("Loading configs {}", settings)
    workflow = SyncAllNotesWorkflow(settings.directory_hierarchy_settings_path)
    workflow.execute()


class TaskName(str, Enum):
    """All avaliable tasks"""

    sync_all = "sync_all"  # pylint: disable=invalid-name


def main(
    task_name: TaskName,
):
    """Main function for running app"""
    task_name_to_func = {"sync_all": sync_all_hackmd_notes_to_github}
    task_name_to_func[task_name]()


if __name__ == "__main__":
    typer.run(main)
