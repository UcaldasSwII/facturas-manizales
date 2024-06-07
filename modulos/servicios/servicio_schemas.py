from pydantic import BaseModel
from typing import Optional
from enum import Enum
from modulos.servicios.servicio_model import ListaServicios

class ListaServicios(str, Enum):
    AGUAS_DE_MANIZALES = "AGUAS DE MANIZALES"
    EFIGAS = "EFIGAS"
    CHEC = "CHEC"

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