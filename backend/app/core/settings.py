from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_ROOT = BACKEND_DIR.parent


class Settings(BaseSettings):
    APP_NAME: str = "Orion AI Studio"
    APP_VERSION: str = "0.1.0"
    APP_ENV: str = "development"
    DEBUG: bool = True

    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    DATABASE_URL: str = (
        "postgresql+psycopg://postgres:postgres@localhost:5432/orion"
    )

    PROJECT_ROOT: Path = PROJECT_ROOT
    BACKEND_PATH: Path = BACKEND_DIR
    WORKSPACE_PATH: Path = PROJECT_ROOT / "workspace"
    MEMORY_PATH: Path = PROJECT_ROOT / "memory"
    LOGS_PATH: Path = PROJECT_ROOT / "logs"
    CONFIG_PATH: Path = PROJECT_ROOT / "config"
    DOCS_PATH: Path = PROJECT_ROOT / "docs"

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()