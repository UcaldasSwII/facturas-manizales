from pydantic import BaseModel

class PagoBase(BaseModel):
    factura_id: int
    monto: float
    metodo: str

class PagoCreate(PagoBase):
    pass

class Pago(PagoBase):
    id: int

    class Config:
        orm_mode = True
