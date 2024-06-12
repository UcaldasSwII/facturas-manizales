from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .servicio_service import registrar_servicio, obtener_servicio_por_codigo_service, get_servicios_inDB, eliminar_servicio_service
from .servicio_service import obtener_id_por_codigo_service, obtener_servicios_usuario_service
from .servicio_schemas import ServicioCreate
from config.db import get_db
from .servicio_model import ListaServicios
from fastapi.encoders import jsonable_encoder

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
    servicio = obtener_servicio_por_codigo_service(codigo_suscriptor, db)
    if servicio:
        return JSONResponse(content=jsonable_encoder(servicio), status_code=200)
    else:
        return JSONResponse(content={"message": "Servicio no encontrado"}, status_code=404)
    
#get todos los servicios
@router.get("/")
def obtener_servicios(db: Session = Depends(get_db)):
    out_servicios = get_servicios_inDB(db)
    if out_servicios:
        return JSONResponse(content=jsonable_encoder(out_servicios), status_code=200)
    else:
        return JSONResponse(content={"message": "No hay servicios registrados"}, status_code=404)

#eliminar servicio por codigo_suscriptor
@router.delete("/{codigo_suscriptor}")
def eliminar_servicio(codigo_suscriptor: int, db: Session = Depends(get_db)):
    servicio = eliminar_servicio_service(codigo_suscriptor, db)
    if servicio:
        return JSONResponse(content={"message": "Servicio eliminado"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Servicio no encontrado"}, status_code=404)
    
#obtener id del servicio
@router.get("/id/{codigo_suscriptor}")
def obtener_id_servicio(codigo_suscriptor: int, db: Session = Depends(get_db)):
    servicio_id = obtener_id_por_codigo_service(codigo_suscriptor, db)
    if servicio_id:
        return JSONResponse(content={"id": servicio_id}, status_code=200)
    else:
        return JSONResponse(content={"message": "Servicio no encontrado"}, status_code=404)
    

#Obtener todos los servicios relacionados con un usuario_id
@router.get("/usuario/{usuario_id}")
def obtener_servicios_usuario(usuario_id: int, db: Session = Depends(get_db)):
    out_servicios = obtener_servicios_usuario_service(usuario_id, db)
    if out_servicios:
        return JSONResponse(content=jsonable_encoder(out_servicios), status_code=200)
    else:
        return JSONResponse(content={"message": "usuario no tiene servicios registrados"}, status_code=404)