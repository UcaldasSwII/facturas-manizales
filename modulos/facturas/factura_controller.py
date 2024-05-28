from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .factura_service import FacturaService
from .factura_repository import FacturaRepository
from .factura_schemas import FacturaCreate, Factura
from modulos.common.database import get_db

router = APIRouter()

@router.post("/facturas/", response_model=Factura)
def crear_factura(factura: FacturaCreate, db: Session = Depends(get_db)):
    repo = FacturaRepository(db)
    service = FacturaService(repo)
    return service.registrar_factura(factura)

@router.get("/facturas/{factura_id}", response_model=Factura)
def obtener_factura(factura_id: int, db: Session = Depends(get_db)):
    repo = FacturaRepository(db)
    factura = repo.obtener_factura(factura_id)
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return factura
