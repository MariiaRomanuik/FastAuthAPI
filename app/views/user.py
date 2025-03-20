from sqlalchemy.orm import Session
from app import controllers, schemas, database
from fastapi import APIRouter, Depends

router = APIRouter()


def get_db():
    db = database.connection.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.user.User)
def create_user(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    return controllers.user.create_user(db=db, user=user)


@router.get("/", response_model=list[schemas.user.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return controllers.user.get_users(db=db, skip=skip, limit=limit)
