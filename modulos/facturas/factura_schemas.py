from pydantic import BaseModel
from datetime import date

class FacturaBase(BaseModel):
    consumo: float
    costo: float
    estado: str
    fecha_pago: date
    servicio_id: int

class FacturaCreate(FacturaBase):
    pass

class Factura(FacturaBase):
    id_factura: int

    class Config:
        from_atributes = True
