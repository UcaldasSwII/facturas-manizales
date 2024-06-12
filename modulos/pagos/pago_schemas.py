from pydantic import BaseModel

class PagoBase(BaseModel):
    tipo_pago: str
    monto: float
    factura_id: int

class PagoCreate(PagoBase):
    pass

class Pago(PagoBase):
    id_pago: int

    class Config:
        from_atributes = True
