from .pago_repository import PagoRepository
from .pago_model import Pago
from .pago_schemas import PagoCreate

class PagoService:
    def __init__(self, repo: PagoRepository):
        self.repo = repo

    def registrar_pago(self, pago_data: PagoCreate):
        nuevo_pago = Pago(**pago_data.dict())
        return self.repo.agregar_pago(nuevo_pago)
