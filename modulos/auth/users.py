from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, relationship
from config.db import Base
from passlib.hash import bcrypt

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    servicios = relationship("Servicio", back_populates="usuario")

def create_user(db: Session, user: User):
    password = bcrypt.hash(user.password)
    db_user = User(username=user.username, email=user.email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
