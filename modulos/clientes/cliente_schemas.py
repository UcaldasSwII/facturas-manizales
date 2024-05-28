from pydantic import BaseModel

class ClienteBase(BaseModel):
    nombre: str
    email: str
    telefono: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True
