from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .pago_service import registrar_pago, get_pagos_inDB, eliminar_pago_service, obtener_pagos_usuario_service
from .pago_schemas import PagoCreate
from config.db import get_db
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/pagos", tags=["pagos"])

@router.post("/")
def crear_pago(pago: PagoCreate, db: Session = Depends(get_db)):
    new_pago = registrar_pago(pago, db)
    if new_pago:
        return JSONResponse(content={"message": "Pago creado"}, status_code=201)
    else:
        raise JSONResponse(content={"message": "Pago no creado"}, status_code=400)

#obtener todos los pagos
@router.get("/")
def obtener_pagos(db: Session = Depends(get_db)):
    out_pagos = get_pagos_inDB(db)
    if out_pagos:
        return JSONResponse(content={"pagos": [pago.__dict__ for pago in out_pagos]}, status_code=200)
    else:
        return JSONResponse(content={"message": "No hay pagos registrados"}, status_code=404)
    
#obtener todos los pagos de un usuario
@router.get("/{usuario_id}")
def obtener_pagos_usuario(usuario_id: int, db: Session = Depends(get_db)):
    pagos = obtener_pagos_usuario_service(usuario_id, db)
    if pagos:
        return JSONResponse(content={"pagos": [pago.__dict__ for pago in pagos]}, status_code=200)
    else:
        return JSONResponse(content={"message": "No hay pagos registrados"}, status_code=404)
    
#eliminar pago por id
@router.delete("/{id_pago}")
def eliminar_pago(id_pago: int, db: Session = Depends(get_db)):
    pago = eliminar_pago_service(id_pago, db)
    if pago:
        return JSONResponse(content={"message": "Pago eliminado"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Pago no encontrado"}, status_code=404)

