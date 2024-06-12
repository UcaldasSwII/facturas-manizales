from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from enum import Enum as PyEnum
class ListaServicios(PyEnum):
    AGUAS_DE_MANIZALES = "AGUAS DE MANIZALES"
    EFIGAS = "EFIGAS"
    CHEC = "CHEC"

class Servicio(Base):
    __tablename__ = 'servicios'
    servicio_id = Column(Integer, primary_key=True, index=True)
    codigo_suscripcion = Column(Integer, index=True, unique=True)
    nombre = Column(String, index=True)
    tipo = Column(Enum(ListaServicios))
    usuario_id = Column(Integer, ForeignKey('users.id'))
    facturas = relationship("Factura", back_populates="servicio")
    usuario = relationship("User", back_populates="servicios")
