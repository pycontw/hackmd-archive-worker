"""App configuration"""
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Settings for app"""

    directory_hierarchy_settings_path: Path = (
        Path(__file__).parent.parent / "directory_hierarchy.yaml"
    )

    class Config:  # pylint: disable=too-few-public-methods
        """Settings Config"""

        env_file = ".env"
        env_file_encoding = "utf-8"
