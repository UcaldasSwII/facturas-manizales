from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .factura_service import registrar_factura, obtener_factura_por_id_service ,editar_estado_factura_service
from .factura_service import get_facturas_inDB, eliminar_factura_service, obtener_facturas_por_servicio_id_service
from .factura_schemas import FacturaCreate, Factura
from config.db import get_db
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/facturas/", response_model=Factura)
def crear_factura(factura: FacturaCreate, db: Session = Depends(get_db)):
    new_factura = registrar_factura(factura, db)
    if new_factura:
        return JSONResponse(content={"message": "Factura creada"}, status_code=201)
    else:
        return JSONResponse(content={"message": "Factura no creada"}, status_code=400)

#obetener todas las facturas
@router.get("/facturas/", response_model=Factura)
def obtener_facturas(db: Session = Depends(get_db)):
    out_facturas = get_facturas_inDB(db)
    if out_facturas:
        return JSONResponse(content={"facturas": [factura.__dict__ for factura in out_facturas]}, status_code=200)
    else:
        return JSONResponse(content={"message": "No hay facturas registradas"}, status_code=404)

#Eliminar factura por id
@router.get("/facturas/{factura_id}", response_model=Factura)
def obtener_factura(factura_id: int, db: Session = Depends(get_db)):
    factura = eliminar_factura_service(factura_id, db)
    if factura:
        return JSONResponse(content={"message": "Factura eliminada"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Factura no encontrada"}, status_code=404)

#Editar estado de la factura
@router.put("/facturas/{factura_id}")
def editar_estado_factura(factura_id: int, db: Session = Depends(get_db)):
    factura = editar_estado_factura_service(factura_id, db)
    if factura:
        return JSONResponse(content={"message": "Factura pagada"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Factura no encontrada"}, status_code=404)
    
#obtener factura por servicio_id
@router.get("/facturas/servicio/{servicio_id}", response_model=Factura)
def obtener_factura_por_servicio_id(servicio_id: int, db: Session = Depends(get_db)):
    factura = obtener_facturas_por_servicio_id_service(servicio_id, db)
    if factura:
        return JSONResponse(content={"factura": factura.__dict__}, status_code=200)
    else:
        return JSONResponse(content={"message": "Factura no encontrada"}, status_code=404)