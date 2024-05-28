from sqlalchemy import Column, Integer, String
from modulos.common.database import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefono = Column(String, index=True)
