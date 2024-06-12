
from sqlalchemy.orm import Session

from modulos.auth.auth_schemas import User as UserCreate
from modulos.auth.auth_model import User as UserModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_inDB(db:Session):
    users = db.query(UserModel).all()
    out_users = [UserCreate(**user.__dict__) for user in users]
    return out_users
    
def get_user_by_username(username:str, db:Session):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    return user


def create_user(user_data: UserCreate, db: Session):
    # Encriptar la contraseña del usuario
    hashed_password = pwd_context.hash(user_data.password)
    # Crear una instancia del modelo de usuario con la contraseña encriptada
    user = UserModel(username=user_data.username, email=user_data.email, name=user_data.name, password=hashed_password)
    # Agregar el nuevo usuario a la sesión de la base de datos
    db.add(user)
    # Confirmar la transacción
    db.commit()
    # Refrescar la instancia del usuario para obtener los datos guardados
    db.refresh(user)
    return user

def delete_user(username: str, db:Session):
    user = get_user_by_username(username,db)
    if user:
        db.delete(user)
        db.commit()
        return True
    else:
        return False