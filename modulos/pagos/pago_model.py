from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from modulos.common.database import Base

class Pago(Base):
    __tablename__ = 'pagos'
    id = Column(Integer, primary_key=True, index=True)
    factura_id = Column(Integer, ForeignKey('facturas.id'))
    monto = Column(Float)
    metodo = Column(String)
    factura = relationship("Factura")
