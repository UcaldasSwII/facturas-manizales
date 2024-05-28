from .cliente_repository import ClienteRepository
from .cliente_model import Cliente
from .cliente_schemas import ClienteCreate

class ClienteService:
    def __init__(self, repo: ClienteRepository):
        self.repo = repo

    def registrar_cliente(self, cliente_data: ClienteCreate):
        nuevo_cliente = Cliente(**cliente_data.dict())
        return self.repo.agregar_cliente(nuevo_cliente)
    
    def listar_clientes(self):
        return self.repo.listar_clientes()
    
    def actualizar_cliente(self, cliente_id: int, cliente_data: ClienteCreate):
        return self.repo.actualizar_cliente(cliente_id, cliente_data)
    
    def eliminar_cliente(self, cliente_id: int):
        return self.repo.eliminar_cliente(cliente_id)