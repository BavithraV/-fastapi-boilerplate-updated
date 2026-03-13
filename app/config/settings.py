from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

class Settings(BaseSettings):

    PROJECT_NAME: str = "DM Reporter Rating AI"
    VERSION: str = "1.0"

    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4o-mini"

    class Config:
        env_file = ".env"


settings = Settings()