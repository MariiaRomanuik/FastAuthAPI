from sqlalchemy.orm import Session
from app.models.user import User
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.utils.security import verify_token, pwd_context
from app.database.connection import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    email: str = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user = get_user(db, email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email)
    if user is None:
        return None
    if not verify_password(password, user.password):
        return None
    return user
