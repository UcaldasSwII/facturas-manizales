from pydantic import BaseModel
from typing import Optional
from enum import Enum
from modulos.servicios.servicio_model import ListaServicios

class ServicioBase(BaseModel):
    codigo_suscripcion: int
    nombre: str
    tipo: ListaServicios
    usuario_id: int

    class config:
        from_atributes = True

class ServicioCreate(ServicioBase):
    pass

