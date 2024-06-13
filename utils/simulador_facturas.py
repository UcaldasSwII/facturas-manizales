#Clase para generar facturas de forma aleatoria
#Crea instancias de la clase Factura con valores aleatorios para los campos:
#    consumo = un nmero del 40 al 100
#    costo = un float del 30000 al 600000
#    estado = Siempre PENDIENTE
#   fecha_pago = La fecha actual + un numero de dias aleatorio entre 1 y 30
# El metodo GenerarFactura recibe un id de servicio y retorna una instancia de la clase Factura

import random
from datetime import datetime, timedelta
from modulos.facturas.factura_schemas import FacturaCreate

class SimuladorFacturas:
    def __init__(self):
        self.consumo = random.randint(40, 100)
        self.costo = random.uniform(30000, 600000)
        self.estado = "PENDIENTE"
        self.fecha_pago = (datetime.now() + timedelta(days=random.randint(1, 30))).date().strftime("%Y-%m-%d")

    
    #Retorna un dict
    def generar_factura(self, servicio_id: int):
        return FacturaCreate(consumo=self.consumo, costo=self.costo, estado=self.estado, fecha_pago=self.fecha_pago, servicio_id=servicio_id)
    
