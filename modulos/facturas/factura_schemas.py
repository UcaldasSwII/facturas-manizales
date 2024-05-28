from pydantic import BaseModel

class FacturaBase(BaseModel):
    cliente_id: int
    total: float
    status: str

class FacturaCreate(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int

    class Config:
        orm_mode = True
