
from .servicio_model import Servicio
from .servicio_schemas import ServicioCreate
from sqlalchemy.orm import Session



def registrar_servicio(servicio_data: ServicioCreate, db: Session):
    nuevo_servicio = Servicio(**servicio_data.dict())
    db.add(nuevo_servicio)
    db.commit()
    db.refresh(nuevo_servicio)
    return nuevo_servicio

def obtener_servicio_por_codigo_service(codigo_suscriptor: int, db: Session):
    servicio = db.query(Servicio).filter(Servicio.codigo_suscripcion == codigo_suscriptor).first()
    return servicio
