from pydantic import BaseModel, Field


# Clase de esquema para la estructura de los datos de usuario
class User(BaseModel):
    username: str 
    email: str = Field(pattern="^([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)$", default="no@mail.com")
<<<<<<<< HEAD:modulos/users/users_schemas.py
    password: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
========
    name: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
>>>>>>>> master:modulos/users/auth_schemas.py
