from .servicio_repository import ServicioRepository
from .servicio_model import Servicio
from .servicio_schemas import ServicioCreate

class ServicioService:
    def __init__(self, repo: ServicioRepository):
        self.repo = repo

    def registrar_servicio(self, servicio_data: ServicioCreate):
        nuevo_servicio = Servicio(**servicio_data.dict())
        return self.repo.agregar_servicio(nuevo_servicio)
