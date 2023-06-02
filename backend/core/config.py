# config.py
import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Ornaman Backend"
    PROJECT_DESC: str = "Just Another Ornaman Web Service (Backend)"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_SERVER: str = [
        {"url": "http://127.0.0.1:8000", "description": "Development Server"},
        {
            "url": "http://localhost:8000/",
            "description": "Another url alternatives",
        },
        {
            "url": "[REPLACE WITH PRODUCTION URL]",  # TODO REPLACE WITH PRODUCTION URL
            "description": "Production Server",
        },
    ]
    # Database Config
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv(
        "POSTGRES_PORT", 5432
    )  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    # JWT Authentication Config
    SECRET_KEY: str = os.getenv("SECRET_KEY")  #
    ALGORITHM = "HS256"  # type of algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in minutes


settings = Settings()
