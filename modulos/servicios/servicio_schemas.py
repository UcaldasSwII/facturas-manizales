from pydantic import BaseModel

class ServicioBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float

class ServicioCreate(ServicioBase):
    pass

class Servicio(ServicioBase):
    id: int

    class Config:
        orm_mode = True
