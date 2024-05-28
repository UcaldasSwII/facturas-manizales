from fastapi import FastAPI 
#from dotenv import load_dotenv
from modulos.clientes.cliente_controller import router as cliente_router
from modulos.servicios.servicio_controller import router as servicio_router
from modulos.facturas.factura_controller import router as factura_router
from modulos.pagos.pago_controller import router as pago_router
from modulos.common.database import init_db

#load_dotenv()

app = FastAPI()

app.include_router(cliente_router, prefix="/api")
app.include_router(servicio_router, prefix="/api")
app.include_router(factura_router, prefix="/api")
app.include_router(pago_router, prefix="/api")

@app.on_event("startup")
def on_startup():
    init_db()

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)