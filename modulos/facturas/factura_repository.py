from sqlalchemy.orm import Session
from .factura_model import Factura

class FacturaRepository:
    def __init__(self, db: Session):
        self.db = db

    def agregar_factura(self, factura: Factura):
        self.db.add(factura)
        self.db.commit()
        self.db.refresh(factura)
        return factura

    def obtener_factura(self, factura_id: int):
        return self.db.query(Factura).filter(Factura.id == factura_id).first()
