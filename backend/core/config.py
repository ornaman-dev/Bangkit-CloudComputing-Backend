# core > config.py
import os
from pathlib import Path

from dotenv import load_dotenv

# env_path = Path(".") / ".env"  # local env
env_path = Path(".") / ".envgcp"  # try GCP env
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Ornaman Backend"
    PROJECT_DESC: str = "Just Another Ornaman Web Service (Backend)"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_SERVER: str = [
        {
            "url": "https://ornamanbackend-1-j5052767.deta.app",
            "description": "for online test",
        },
        {"url": "http://127.0.0.1:8000", "description": "Development Server"},
        {
            "url": "http://localhost:8000/",
            "description": "Another Local Host url alternatives",
        },
        {
            "url": "[REPLACE WITH PRODUCTION URL]",  # TODO REPLACE WITH PRODUCTION URL
            "description": "Production Server",
        },
    ]
    ORIGIN_DOMAIN_ALLOWED: str = [
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1" "http://127.0.0.1:8000",
        "https://ornaman.com",
        "https://api.ornaman.com",
        "https://ornamanbackend-1-j5052767.deta.app",
    ]
    # Database Config
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "ornaman_backend_db")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    # JWT Authentication Config
    SECRET_KEY: str = os.getenv("SECRET_KEY")  #
    ALGORITHM = "HS256"  # type of algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in minutes
    # for Unit test for JWT token header
    TEST_USER_EMAIL = "testuser@ornaman.com"


settings = Settings()
