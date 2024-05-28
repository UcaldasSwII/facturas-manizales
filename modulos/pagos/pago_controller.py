from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .pago_service import PagoService
from .pago_repository import PagoRepository
from .pago_schemas import PagoCreate, Pago
from modulos.common.database import get_db

router = APIRouter()

@router.post("/pagos/", response_model=Pago)
def crear_pago(pago: PagoCreate, db: Session = Depends(get_db)):
    repo = PagoRepository(db)
    service = PagoService(repo)
    return service.registrar_pago(pago)

@router.get("/pagos/{pago_id}", response_model=Pago)
def obtener_pago(pago_id: int, db: Session = Depends(get_db)):
    repo = PagoRepository(db)
    pago = repo.obtener_pago(pago_id)
    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return pago
