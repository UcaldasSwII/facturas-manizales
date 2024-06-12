from fastapi import Request,HTTPException
from fastapi.security import HTTPBearer

from utils.jwt_manage import decode_jwt

from modulos.auth.auth_service import get_user_by_username
from config.db import get_db
from fastapi import Depends

# Clase para manejar el token JWT

class JWTBearer(HTTPBearer):

    async def __call__(self, request: Request, db = Depends(get_db)):
        credentials = await super().__call__(request)
        
        data = decode_jwt(credentials.credentials)
        
        if data:
            
            user = get_user_by_username(data["username"] ,db)
            
            if user:
                return user
            else:
                raise HTTPException(status_code=403, detail="Invalid authorization code")
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")

