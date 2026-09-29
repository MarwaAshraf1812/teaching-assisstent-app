from fastapi import APIRouter, Depends

from src.helpers.config import Settings, get_settings


base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)


@base_router.get("/")
def welcome(
    app_settings: Settings = Depends(get_settings),
):
    return {
        "message": f"Welcome to the {app_settings.APP_NAME} app!",
        "version": app_settings.APP_VERSION,
    }