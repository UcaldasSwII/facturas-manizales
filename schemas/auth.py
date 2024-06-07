from pydantic import BaseModel
from pydantic import Field


# Clase de esquema para la estructura de los datos de usuario
class User(BaseModel):
    username: str = Field(max_length=50)
    email: str = Field(pattern="^([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)$", default="no@mail.com")
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
