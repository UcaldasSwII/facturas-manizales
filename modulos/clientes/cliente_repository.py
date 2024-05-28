from sqlalchemy.orm import Session
from .cliente_model import Cliente

class ClienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def agregar_cliente(self, cliente: Cliente):
        self.db.add(cliente)
        self.db.commit()
        self.db.refresh(cliente)
        return cliente
    
    def obtener_cliente(self, cliente_id: int):
        return self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
    
    def listar_clientes(self):
        return self.db.query(Cliente).all()
    
    def actualizar_cliente(self, cliente_id: int, cliente_data):
        cliente = self.obtener_cliente(cliente_id)
        if not cliente:
            return None
        for key, value in cliente_data.dict().items():
            setattr(cliente, key, value)
        self.db.commit()
        self.db.refresh(cliente)
        return cliente
    
    def eliminar_cliente(self, cliente_id: int):
        cliente = self.obtener_cliente(cliente_id)
        if not cliente:
            return None
        self.db.delete(cliente)
        self.db.commit()
        return cliente