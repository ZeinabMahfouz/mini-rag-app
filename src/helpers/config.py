import os
from pydantic_settings import BaseSettings, SettingsConfigDict

# تحديد مسار المجلد الرئيسي حيث يقع ملف .env بدقة
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
env_file_path = os.path.join(base_dir, ".env")

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    # الطريقة الصحيحة والمعتمدة في Pydantic v2 لقراءة ملف الـ .env
    model_config = SettingsConfigDict(env_file="/mnt/d/My projects/LLM-Projects/mini-rag-app/src/.env", extra="ignore")

def get_settings():
    return Settings()
