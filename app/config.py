"""App configuration"""
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Settings for app"""

    directory_hierarchy_settings_path: Path = (
        Path(__file__).parent / "directory_hierarchy.yaml"
    )

    MEILISEARCH_HOST: Optional[str] = "http://meilisearch"
    MEILISEARCH_PORT: Optional[int] = 7700
    MEILISEARCH_MASTER_KEY: Optional[str] = None

    class Config:  # pylint: disable=too-few-public-methods
        """Settings Config"""

        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()
