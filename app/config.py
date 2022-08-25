"""App configuration"""
from pathlib import Path
from typing import Optional

from loguru import logger
from pydantic import AnyHttpUrl, BaseSettings, HttpUrl


class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Settings for app"""

    directory_hierarchy_settings_path: Path = (
        Path(__file__).parent / "directory_hierarchy.yaml"
    )

    MEILISEARCH_URL: AnyHttpUrl = "http://meilisearch:7700"
    MEILISEARCH_MASTER_KEY: Optional[str] = None
    HACKMD_URL: HttpUrl = "https://hackmd.io/team/pycontw/exportAllNotes"
    HACKMD_COOKIE: Optional[str] = None

    class Config:  # pylint: disable=too-few-public-methods
        """Settings Config"""

        env_file = ".env"
        env_file_encoding = "utf-8"


logger.info("Loading configs")
config = Settings()
logger.debug("Loaded configs {}", config)
logger.info("Configs loaded successfully")
