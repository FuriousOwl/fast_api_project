from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.settings import settings

engin = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)

Base = declarative_base()


def get_session():
    with SessionLocal() as session:
        yield session
