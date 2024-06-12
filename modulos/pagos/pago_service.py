
from .pago_model import Pago
from .pago_schemas import PagoCreate
from sqlalchemy.orm import Session

#TODO: cuando se crea un pago hay que buscar la factura y cambiar el estado
def registrar_pago(pago_data: PagoCreate, db: Session):
    nuevo_pago = Pago(**pago_data.dict())
    db.add(nuevo_pago)
    db.commit()
    db.refresh(nuevo_pago)
    return nuevo_pago

def obtener_pagos_usuario_service(usuario_id: int, db: Session):
    pagos = db.query(Pago).filter(Pago.usuario_id == usuario_id).all()
    return pagos

def eliminar_pago_service(id_pago: int, db: Session):
    pago = db.query(Pago).filter(Pago.id_pago == id_pago).first()
    if pago:
        db.delete(pago)
        db.commit()
        return True
    else:
        return False

def get_pagos_inDB(db: Session):
    pagos = db.query(Pago).all()
    return pagos


