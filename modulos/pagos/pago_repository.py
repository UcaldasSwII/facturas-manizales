from sqlalchemy.orm import Session
from .pago_model import Pago

class PagoRepository:
    def __init__(self, db: Session):
        self.db = db

    def agregar_pago(self, pago: Pago):
        self.db.add(pago)
        self.db.commit()
        self.db.refresh(pago)
        return pago

    def obtener_pago(self, pago_id: int):
        return self.db.query(Pago).filter(Pago.id == pago_id).first()
