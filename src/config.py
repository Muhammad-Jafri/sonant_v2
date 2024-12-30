import os
from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))


class Settings(BaseSettings):
    OPENAI_API_KEY: str = Field(..., env='OPENAI_API_KEY')
    TTS_MODEL_PATH: str = Field(..., env='TTS_MODEL_PATH')
    ASR_MODEL_PATH: str = Field(..., env='ASR_MODEL_PATH')

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '..', '.env')
        env_file_encoding = 'utf-8'


settings = Settings()
