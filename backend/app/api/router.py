from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "Welcome to Orion AI Studio",
    }


@router.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
    }