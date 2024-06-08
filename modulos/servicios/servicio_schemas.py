from pydantic import BaseModel
from typing import Optional
from enum import Enum
from modulos.servicios.servicio_model import ListaServicios

class ServicioBase(BaseModel):
    nombre: str
    tipo: ListaServicios
    usuario_id: int

class ServicioCreate(ServicioBase):
    pass

class Servicio(ServicioBase):
    codigo_suscripcion: int

    class Config:
        orm_mode = True
