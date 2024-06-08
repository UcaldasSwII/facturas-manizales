
from sqlalchemy.orm import Session

<<<<<<< HEAD:modulos/users/users_service.py
from modulos.users.auth_schemas import UserLogin
from modulos.users.users_model import User as UserModel
from modulos.users.users_schemas import UserCreate
=======
from modulos.auth.auth_schemas import User
from modulos.auth.auth_model import User as UserModel
>>>>>>> master:modulos/auth/users_service.py

def get_user_inDB(db:Session):
    users = db.query(UserModel).all()
    out_users = [UserCreate(**user.__dict__) for user in users]
    return out_users
    
def get_user_by_username(username:str, db:Session):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    return user

def create_new_user(new_user:UserCreate, db:Session):
    db_user = UserModel(**new_user.__dict__)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user