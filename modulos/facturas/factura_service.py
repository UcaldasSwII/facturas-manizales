
from .factura_model import Factura
from .factura_schemas import FacturaCreate
from sqlalchemy.orm import Session


def registrar_factura(factura_data: FacturaCreate, db: Session):
    nueva_factura = Factura(**factura_data.dict())
    return nueva_factura

def obtener_factura_por_id_service(factura_id: int, db: Session):
    factura = db.query(Factura).filter(Factura.id_factura == factura_id).first()
    return factura

def get_facturas_inDB(db: Session):
    facturas = db.query(Factura).all()
    out_facturas = [FacturaCreate(**factura.__dict__) for factura in facturas]
    return facturas

def eliminar_factura_service(factura_id: int, db: Session):
    factura = db.query(Factura).filter(Factura.id_factura == factura_id).first()
    if factura:
        db.delete(factura)
        db.commit()
        return True
    else:
        return False
    
def editar_estado_factura_service(factura_id: int, db: Session):
    factura = db.query(Factura).filter(Factura.id_factura == factura_id).first()
    if factura:
        factura.estado = "Pagada"
        db.commit()
        return True
    else:
        return False
    
def obtener_facturas_por_servicio_id_service(servicio_id: int, db: Session):
    factura = db.query(Factura).filter(Factura.servicio_id == servicio_id).first()
    if factura:
        return factura
    else:
        return False