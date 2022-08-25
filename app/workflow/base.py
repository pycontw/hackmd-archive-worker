"""Base workflow"""
from pathlib import Path

import yaml
from loguru import logger


class BaseWorkflow:  # pylint: disable=too-few-public-methods
    """Base workflow used for all archiving operations"""

    def __init__(self, configuration_path: Path):
        logger.info("Initializing {}", self.__class__.__name__)
        self.setting_path: Path = configuration_path
        with open(self.setting_path.resolve(), "r") as setting_file:
            self.directory_hierarchy_setting = yaml.load(
                setting_file, Loader=yaml.CLoader
            )
        self.output_path = Path(self.directory_hierarchy_setting["output_dir"])
        logger.debug("Loaded output setting: {}", self.directory_hierarchy_setting)

    def download_notes(self):  # pylint: disable=no-self-use
        """Download notes"""
        return NotImplementedError

    def classify_notes(self):  # pylint: disable=no-self-use
        """Classify notes into correct folder position"""
        return NotImplementedError

    def build_index(self):  # pylint: disable=no-self-use
        """Create index for archived notes"""
        return NotImplementedError

    def index_notes(self):  # pylint: disable=no-self-use
        """Index the notes into Meilisearch"""
        return NotImplementedError

    def execute(self):  # pylint: disable=no-self-use
        """Execute workflow"""
        return NotImplementedError
