from collections.abc import Generator

from config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
