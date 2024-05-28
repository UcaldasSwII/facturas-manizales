from sqlalchemy import Column, Integer, String, Float
from modulos.common.database import Base

class Servicio(Base):
    __tablename__ = 'servicios'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, index=True)
    precio = Column(Float, index=True)
