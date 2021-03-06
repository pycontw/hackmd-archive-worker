"""Main module for running app"""
from enum import Enum
import time
from datetime import timedelta

import typer
from config import config
from loguru import logger
from workflow.sync_all_notes_workflow import SyncAllNotesWorkflow


def sync_all_hackmd_notes(enable_index: bool = False):
    """Sync all hackmd notes to github"""
    while True:
        try:
            logger.info("Start to sync all hackmd notes to github")
            logger.debug("Loading configs {}", config)
            workflow = SyncAllNotesWorkflow(config.directory_hierarchy_settings_path)
            workflow.execute(enable_index=enable_index)
        except KeyboardInterrupt:
            logger.error("Keyboard interrupt")
            raise
        except Exception:  # pylint: disable=broad-except
            logger.exception("Exception in shopify worker")
        time.sleep(timedelta(days=1).total_seconds())


def build_hackmd_index():
    """Build index for hackmd notes"""
    logger.info("Start to build index")
    logger.debug("Loading configs {}", config)
    workflow = SyncAllNotesWorkflow(config.directory_hierarchy_settings_path)
    workflow.execute_hackmd_index()


class TaskName(str, Enum):
    """All avaliable tasks"""

    sync_all_notes = "sync_all_notes"  # pylint: disable=invalid-name
    build_index = "build_index"  # pylint: disable=invalid-name


def main(
    task_name: TaskName,
    enable_index: bool = False,
):
    """Main function for running app"""
    task_name_to_func = {
        "sync_all_notes": lambda: sync_all_hackmd_notes(enable_index),
        "build_index": build_hackmd_index,
    }
    task_name_to_func[task_name]()


if __name__ == "__main__":
    typer.run(main)
