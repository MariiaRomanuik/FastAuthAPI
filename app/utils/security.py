import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from typing import Dict
from passlib.context import CryptContext
from app.config import SECRET_KEY, ALGORITHM


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def create_access_token(data: Dict, expires_delta: timedelta = timedelta(hours=1)) -> str:
    """
    Create a new JWT access token for the user with the given data (payload).

    :param data: Dictionary of user-related data (e.g., {'sub': 'username'})
    :param expires_delta: Optional timedelta for token expiration (default is 1 hour)
    :return: Encoded JWT token string
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})  # Add the expiration timestamp

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


