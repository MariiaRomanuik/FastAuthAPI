from fastapi import FastAPI
from app.views import user
from app.views import auth
from app.database.connection import init_db

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth")
