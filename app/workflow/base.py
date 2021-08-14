"""Base workflow"""
from pathlib import Path

import yaml
from loguru import logger


class BaseWorkflow:  # pylint: disable=too-few-public-methods
    """Base workflow used for all archiving operations"""

    def __init__(self, setting_path: Path):
        logger.info("Initializing {}", self.__class__.__name__)
        self.setting_path = setting_path
        self.directory_hierarchy_setting = None

    def load_output_setting(self):
        """Load configuration"""
        with open(self.setting_path.resolve(), "r") as setting_file:
            self.directory_hierarchy_setting = yaml.load(
                setting_file, Loader=yaml.CLoader
            )
            logger.debug("Loaded output setting: {}", self.directory_hierarchy_setting)

    def download_notes(self):  # pylint: disable=no-self-use
        """Download notes"""
        return NotImplementedError

    def classify_notes(self):  # pylint: disable=no-self-use
        """Classify notes into correct folder position"""
        return NotImplementedError

    def upload(self):  # pylint: disable=no-self-use
        """Upload notes to the destination for archiving"""
        return NotImplementedError

    def execute(self):  # pylint: disable=no-self-use
        """Execute workflow"""
        logger.info("Executing {}", self.__class__.__name__)
        self.load_output_setting()
        self.download_notes()
        self.classify_notes()
        self.upload()
