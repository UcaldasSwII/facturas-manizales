<<<<<<< HEAD:modulos/users/auth_controller.py
from fastapi import APIRouter, Depends, HTTPException
from passlib.hash import bcrypt
from sqlalchemy.orm import Session
from .jwt_manage import signJWT
from config.db import SessionLocal
from modulos.users.users_model import User
from modulos.users.users_service import create_new_user

auth_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auth_router.post("/user/signup")
async def create_user_endpoint(user: User, db: Session = Depends(get_db)):
    created_user = create_new_user(db, user)
    return signJWT(created_user.username)

@auth_router.post("/user/login")
async def user_login(user: User, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user and bcrypt.verify(user.password, db_user.password):
        return signJWT(db_user.username)
    return {"error": "Invalid login credentials!"}
=======
from fastapi import APIRouter, Depends

from fastapi.responses import JSONResponse

from modulos.auth.auth_schemas import User, UserLogin

from config.db import get_db
from sqlalchemy.orm import Session


from modulos.auth.auth_service import get_user_by_username
from modulos.auth.auth_service import validate_password

auth_router = APIRouter(prefix="/auth",tags=["auth"])


# Ruta para ingreso de un usuario. #TODO: Reformar el código a SOLID
@auth_router.post("/login")
def login(user: UserLogin, db:Session = Depends(get_db)):
    
    db_user = get_user_by_username(user.username,db)

    if db_user:
        
        token = validate_password(db_user, user)
        
        if token:
            return JSONResponse(content={"token": token}, status_code=200)
        else:
            return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)
        
    else:
        return JSONResponse(content={"message": "User does not exist"}, status_code=401)
>>>>>>> master:modulos/auth/auth_controller.py
