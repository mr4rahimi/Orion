from fastapi import FastAPI

from app.api.router import router
from app.core.logger import logger
from app.core.settings import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.include_router(router)

logger.info(
    f"{settings.APP_NAME} v{settings.APP_VERSION} started."
)