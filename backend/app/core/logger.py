import sys
from pathlib import Path

from loguru import logger

from app.core.settings import get_settings

settings = get_settings()

settings.LOGS_PATH.mkdir(parents=True, exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level=settings.LOG_LEVEL,
    colorize=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "{message}"
    ),
)

logger.add(
    Path(settings.LOGS_PATH) / "backend.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level=settings.LOG_LEVEL,
)

logger.add(
    Path(settings.LOGS_PATH) / "errors.log",
    rotation="10 MB",
    retention="60 days",
    compression="zip",
    level="ERROR",
)