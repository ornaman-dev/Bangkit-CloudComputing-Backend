# db > session.py
from typing import Generator

from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database selain SQLite, misal : PostgreSQL (uncomment 2 line)
# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine("mysql://ps369:sup3rs3cr3t@34.124.238.240/ornaman?charset=utf8mb4")

# Database SQLite
# SQLALCHEMY_DATABASE_URL = "sqlite:///./rombak_sql_app.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
