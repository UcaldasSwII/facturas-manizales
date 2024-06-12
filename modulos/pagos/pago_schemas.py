from pydantic import BaseModel

class PagoBase(BaseModel):
    tipo_pago: str
    monto: float
    factura_id: int
    user_id: int

    class Config:
        from_atributes = True

class PagoCreate(PagoBase):
    pass


    
