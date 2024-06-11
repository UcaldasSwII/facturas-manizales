from pydantic import BaseModel
from typing import Optional
from enum import Enum
from modulos.servicios.servicio_model import ListaServicios

class ListaServicios(str, Enum):
    AGUAS_DE_MANIZALES = "AGUAS DE MANIZALES"
    EFIGAS = "EFIGAS"
    CHEC = "CHEC"

class ServicioBase(BaseModel):
    codigo_suscripcion: int
    nombre: str
    tipo: ListaServicios

class ServicioCreate(ServicioBase):
    pass

class Servicio(ServicioBase):
    usuario_id: int

    class Config:
        orm_mode = True
