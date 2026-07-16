from src.controllers.DataController import DataController
from fastapi import FastAPI
from fastapi import APIRouter,Depends,UploadFile,File
from src.helpers.config import get_settings,settings 
from src.controllers import BaseController
import os
data_router = APIRouter(
    prefix="/api/v1/data",tags=["api_v1","data"],
)
@data_router.post("/upload/{project_id}")
async def upload_file(project_id,file: UploadFile = File,app_settings=Depends(get_settings)):
    is_valid = DataController().validate_upload_file(file=file)
    return is_valid