from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from modulos.common.database import Base

class Factura(Base):
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    total = Column(Float)
    status = Column(String)
    cliente = relationship("Cliente")
