from sqlalchemy import Column, Integer, String
from app.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, password={self.password})>"
