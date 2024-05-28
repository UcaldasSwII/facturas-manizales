from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modulos.clientes.cliente_service import ClienteService
from modulos.clientes.cliente_repository import ClienteRepository
from modulos.clientes.cliente_schemas import ClienteCreate, Cliente
from modulos.common.database import get_db

router = APIRouter()

@router.post("/clientes/", response_model=Cliente)
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    repo = ClienteRepository(db)
    service = ClienteService(repo)
    return service.registrar_cliente(cliente)

@router.get("/clientes/{cliente_id}", response_model=Cliente)
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):
    repo = ClienteRepository(db)
    cliente = repo.obtener_cliente(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.get("/listar_clientes/", response_model=list[Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    repo = ClienteRepository(db)
    return repo.listar_clientes()

@router.put("/clientes/{cliente_id}", response_model=Cliente)
def actualizar_cliente(cliente_id: int, cliente: ClienteCreate, db: Session = Depends(get_db)):
    repo = ClienteRepository(db)
    cliente_actualizado = repo.actualizar_cliente(cliente_id, cliente)
    if not cliente_actualizado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente_actualizado

@router.delete("/clientes/{cliente_id}", response_model=Cliente)
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    repo = ClienteRepository(db)
    cliente_eliminado = repo.eliminar_cliente(cliente_id)
    if not cliente_eliminado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente_eliminado