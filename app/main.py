"""Main module for running app"""
import typer
from config import config
from loguru import logger
from workflow.sync_all_notes_workflow import SyncAllNotesWorkflow

app = typer.Typer()


@app.command()
def sync_all_hackmd_notes(enable_index: bool = False):
    """Sync all HackMD notes to github"""
    logger.info("Start to sync all HackMD notes to GitHub")
    workflow = SyncAllNotesWorkflow(
        configuration_path=config.directory_hierarchy_settings_path
    )
    workflow.execute(enable_index=enable_index)


@app.command()
def build_hackmd_index():
    """Build index for HackMD notes"""
    logger.info("Start to build index")
    workflow = SyncAllNotesWorkflow(
        configuration_path=config.directory_hierarchy_settings_path
    )
    workflow.execute_hackmd_index()


if __name__ == "__main__":
    app()
