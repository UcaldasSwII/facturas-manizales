from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .servicio_service import ServicioService
from .servicio_repository import ServicioRepository
from .servicio_schemas import ServicioCreate, Servicio
from modulos.common.database import get_db

router = APIRouter()

@router.post("/servicios/", response_model=Servicio)
def crear_servicio(servicio: ServicioCreate, db: Session = Depends(get_db)):
    repo = ServicioRepository(db)
    service = ServicioService(repo)
    return service.registrar_servicio(servicio)

@router.get("/servicios/{servicio_id}", response_model=Servicio)
def obtener_servicio(servicio_id: int, db: Session = Depends(get_db)):
    repo =  ServicioRepository(db)
    servicio = repo.obtener_servicio(servicio_id)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio
