from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from modulos.auth.auth_schemas import User
from modulos.auth.auth_model import User as UserModel
from modulos.auth.users_service import get_user_by_username,get_user_inDB, create_user as create_user_service, delete_user as delete_user_service

from config.jwt_depends import JWTBearer

from sqlalchemy.orm import Session
from config.db import get_db




users_router = APIRouter(prefix="/users",tags=["usuarios"],)


# Ruta de obtención de la base de datos 
@users_router.get("/")
def get_all_users(db:Session = Depends(get_db)):

    out_users = get_user_inDB(db)

    return JSONResponse(content=jsonable_encoder(out_users), status_code=200)


# Ruta de obtención de un usuario por su username
@users_router.get("/{username}")
def get_user(username: str,db:Session = Depends(get_db) , authorized: UserModel = Depends(JWTBearer())):
    
    user = get_user_by_username(username,db)
    if user:

        return JSONResponse(content=User(**user.__dict__).__dict__, status_code=200)
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)

# Ruta para crear un nuevo usuario. 
@users_router.post("/")
def create_user(user: User, db:Session = Depends(get_db)):
    new_user = create_user_service(user, db)
    if new_user:
        return JSONResponse(content={"message": "User created"}, status_code=201)
    else:
        return JSONResponse(content={"message": "User not created"}, status_code=400)
    

# Ruta para eliminar un usuario
@users_router.delete("/{username}")
def delete_user(username: str, db:Session = Depends(get_db), authorized: UserModel = Depends(JWTBearer())):
    user = get_user_by_username(username,db)
    if user:
        delete_user_service(username,db)
        return JSONResponse(content={"message": "User deleted"}, status_code=200)
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
