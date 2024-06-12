from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .servicio_service import registrar_servicio, obtener_servicio_por_codigo_service
from .servicio_schemas import ServicioCreate
from config.db import get_db
from .servicio_model import ListaServicios

router = APIRouter(prefix="/servicios", tags=["servicios"])

@router.post("/")
def crear_servicio(servicio: ServicioCreate, db: Session = Depends(get_db)):
    # convertir el tipo de servicio que entra como string a un ENUM de ListaServicios
    servicio.tipo = ListaServicios(servicio.tipo)
    new_servicio = registrar_servicio(servicio, db)
    if new_servicio:
        return JSONResponse(content={"message": "Servicio creado"}, status_code=201)
    else:
        return JSONResponse(content={"message": "Servicio no creado"}, status_code=400)

#get servicio por codigo_suscriptor
@router.get("/{codigo_suscriptor}")
def obtener_servicio_por_codigo(codigo_suscriptor: int, db: Session = Depends(get_db)):
    servicio = obtener_servicio_por_codigo_service(codigo_suscriptor)
    if servicio:
        return JSONResponse(content=ServicioCreate(**servicio.__dict__).__dict__, status_code=200)
    else:
        return JSONResponse(content={"message": "Servicio no encontrado"}, status_code=404)
    


