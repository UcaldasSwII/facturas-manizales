from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .pago_service import registrar_pago
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

