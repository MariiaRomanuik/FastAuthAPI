from http.client import HTTPException
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.controllers.auth import authenticate_user, get_current_user
from app.utils.security import create_access_token
from sqlalchemy.orm import Session
from app.database.connection import get_db


router = APIRouter()


@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
def read_users_me(current_user: str = Depends(get_current_user)):
    return {"email": current_user}
