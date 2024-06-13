
from .servicio_model import Servicio
from .servicio_schemas import ServicioCreate
from sqlalchemy.orm import Session
from utils.simulador_facturas import SimuladorFacturas

from modulos.facturas.factura_service import registrar_factura



def registrar_servicio(servicio_data: ServicioCreate, db: Session):
    nuevo_servicio = Servicio(**servicio_data.dict())
    db.add(nuevo_servicio)
    db.commit()
    db.refresh(nuevo_servicio)

    #TODO Cuando se crea un servicio se simula una factura con utils.simulador_facturas

    factura_simulada= SimuladorFacturas().generar_factura(nuevo_servicio.id_servicio)
    registrar_factura(factura_simulada, db)

    return nuevo_servicio

def obtener_servicio_por_codigo_service(codigo_suscriptor: int, db: Session):
    servicio = db.query(Servicio).filter(Servicio.codigo_suscripcion == codigo_suscriptor).first()
    return servicio

def get_servicios_inDB(db: Session):
    servicios = db.query(Servicio).all()
    out_servicios = [ServicioCreate(**servicio.__dict__) for servicio in servicios]
    return out_servicios

def eliminar_servicio_service(codigo_suscriptor: int, db: Session):
    servicio = db.query(Servicio).filter(Servicio.codigo_suscripcion == codigo_suscriptor).first()
    if servicio:
        db.delete(servicio)
        db.commit()
        return True
    else:
        return False

def obtener_id_por_codigo_service(codigo_suscriptor: int, db: Session):
    servicio = db.query(Servicio).filter(Servicio.codigo_suscripcion == codigo_suscriptor).first()
    if servicio:
        return servicio.id_servicio
    else:
        return False
    
def obtener_servicios_usuario_service(usuario_id: int, db: Session):
    servicios = db.query(Servicio).filter(Servicio.usuario_id == usuario_id).all()
    out_servicios = [ServicioCreate(**servicio.__dict__) for servicio in servicios]
    return out_servicios