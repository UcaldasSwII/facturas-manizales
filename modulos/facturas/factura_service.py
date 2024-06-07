from .factura_repository import FacturaRepository
from .factura_model import Factura
from .factura_schemas import FacturaCreate

class FacturaService:
    def __init__(self, repo: FacturaRepository):
        self.repo = repo

    def registrar_factura(self, factura_data: FacturaCreate):
        nueva_factura = Factura(**factura_data.dict())
        return self.repo.agregar_factura(nueva_factura)
