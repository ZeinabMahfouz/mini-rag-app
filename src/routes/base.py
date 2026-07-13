from fastapi import FastAPI
from fastapi import APIRouter
from src.helpers.config import get_settings 

import os
base_router = APIRouter(
    prefix="/api/v1",tags=["api_v1"],
)
@base_router.get("/")
async def welcome():
    app_settings = get_settings()
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {"message": f"Welcome to {app_name}!", "version": app_version}