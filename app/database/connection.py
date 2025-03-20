from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from app.models.base import Base
from fastapi import Depends
from app.config import DATABASE_URL


engine = create_engine(DATABASE_URL, echo=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)

init_db()

def get_db(db: Session = Depends(SessionLocal)):
    """
    Dependency that returns a database session.
    """
    try:
        yield db
    finally:
        db.close()
