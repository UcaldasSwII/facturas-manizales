from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from config.db import Base

class Factura(Base):
    __tablename__ = 'facturas'
    id_factura = Column(Integer, primary_key=True, index=True)
    consumo = Column(Float)
    costo = Column(Float)
    estado = Column(String)
    fecha_pago = Column(Date)
    servicio_id = Column(Integer, ForeignKey('servicios.codigo_suscripcion'))
    pagos = relationship("Pago", back_populates="factura")
    servicio = relationship("Servicio", back_populates="facturas")
