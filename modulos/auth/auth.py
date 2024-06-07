from fastapi import APIRouter, Depends, HTTPException
from passlib.hash import bcrypt
from sqlalchemy.orm import Session
from .jwt_manage import signJWT
from config.db import SessionLocal
from .users_model import User, create_user

auth_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auth_router.post("/user/signup")
async def create_user_endpoint(user: User, db: Session = Depends(get_db)):
    created_user = create_user(db, user)
    return signJWT(created_user.username)

@auth_router.post("/user/login")
async def user_login(user: User, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user and bcrypt.verify(user.password, db_user.hashed_password):
        return signJWT(db_user.username)
    return {"error": "Invalid login credentials!"}
