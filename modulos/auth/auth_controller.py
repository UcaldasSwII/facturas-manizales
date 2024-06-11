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