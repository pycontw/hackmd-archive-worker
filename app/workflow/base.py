"""Base workflow"""
from pathlib import Path
from typing import Optional, Any, Dict

import yaml
from loguru import logger


class BaseWorkflow:  # pylint: disable=too-few-public-methods
    """Base workflow used for all archiving operations"""

    def __init__(self, setting_path: Path):
        logger.info("Initializing {}", self.__class__.__name__)
        self.setting_path: Path = setting_path
        self.directory_hierarchy_setting: Optional[Dict[str, Any]] = None
        self.output_path: Optional[Path] = None

    def load_output_setting(self):
        """Load configuration"""
        with open(self.setting_path.resolve(), "r") as setting_file:
            self.directory_hierarchy_setting = yaml.load(
                setting_file, Loader=yaml.CLoader
            )
            if self.directory_hierarchy_setting:
                self.output_path = Path(self.directory_hierarchy_setting["output_dir"])
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

    def build_index(self):  # pylint: disable=no-self-use
        """Build index for archived notes"""
        return NotImplementedError

    def execute(self, enable_index: bool = False):  # pylint: disable=no-self-use
        """Execute workflow"""
        logger.info("Executing {}", self.__class__.__name__)
        self.load_output_setting()
        self.download_notes()
        self.classify_notes()
        self.upload()
        if enable_index:
            self.build_index()
