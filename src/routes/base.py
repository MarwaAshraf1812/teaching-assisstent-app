from fastapi import APIRouter
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
def welcome(app_settings: Settings = Depends(get_settings)):
    app_settings = get_settings()

    app_name = app_settings.APP_NAME.value
    app_version = app_settings.APP_VERSION.value
    return {"message": f"Welcome to the {app_name} app!", "version": app_version}
