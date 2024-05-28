from sqlalchemy.orm import Session
from .servicio_model import Servicio

class ServicioRepository:
    def __init__(self, db: Session):
        self.db = db

    def agregar_servicio(self, servicio: Servicio):
        self.db.add(servicio)
        self.db.commit()
        self.db.refresh(servicio)
        return servicio

    def obtener_servicio(self, servicio_id: int):
        return self.db.query(Servicio).filter(Servicio.id == servicio_id).first()
