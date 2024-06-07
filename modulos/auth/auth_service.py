
from fastapi import Depends
from modulos.auth.auth_schemas import User, UserLogin
from modulos.auth.auth_model import User as UserModel
from config.db import get_db
from utils.jwt_manage import encode_jwt

from sqlalchemy.orm import Session


from modulos.auth.auth_model import User as UserModel

def get_user_by_username(username: str, db: Session):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    return user
    
def get_token(data: dict):
    return encode_jwt(data)

def validate_password(db_user: UserModel, user:UserLogin):
    if db_user.password == user.password:
            
        token = get_token(User(**db_user.__dict__).__dict__)

        return token
    else:
        return None
