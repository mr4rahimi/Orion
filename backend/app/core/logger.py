import sys

from loguru import logger

from app.core.settings import get_settings

settings = get_settings()

settings.LOGS_PATH.mkdir(parents=True, exist_ok=True)

logger.remove()

LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "{message}"
)

logger.add(
    sys.stdout,
    level=settings.LOG_LEVEL,
    format=LOG_FORMAT,
    colorize=True,
)

logger.add(
    str(settings.LOGS_PATH / "backend.log"),
    level=settings.LOG_LEVEL,
    format=LOG_FORMAT,
    rotation="10 MB",
    retention="30 days",
    enqueue=True,
)

logger.add(
    str(settings.LOGS_PATH / "errors.log"),
    level="ERROR",
    format=LOG_FORMAT,
    rotation="10 MB",
    retention="60 days",
    enqueue=True,
)