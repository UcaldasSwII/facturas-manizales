from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from config.db import Base

class Pago(Base):
    __tablename__ = 'pagos'
    id_pago = Column(Integer, primary_key=True, index=True)
    tipo_pago = Column(String)
    monto = Column(Float)
    factura_id = Column(Integer, ForeignKey('facturas.id_factura'))
    factura = relationship("Factura", back_populates="pagos")
