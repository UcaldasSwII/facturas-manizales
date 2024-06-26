# Librerías requeridas
from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from config.db import Base, engine


from modulos.auth.auth_controller import auth_router
from modulos.auth.user_controller import users_router 
from modulos.servicios.servicio_controller import router as servicio_rotuer
from modulos.pagos.pago_controller import router as pago_router
from modulos.facturas.factura_controller import router as factura_router

# Creación de la aplicación FastAPI
app = FastAPI(title="Facturas_Manizales_Backend", version="0.0.1")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Lista de orígenes permitidos (utiliza dominios específicos en producción)
    allow_credentials=True,
    allow_methods=["*"],  # Métodos HTTP permitidos
    allow_headers=["*"],  # Cabeceras HTTP permitidas
)

# Migración de la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(auth_router, tags=["auth"])
app.include_router(users_router, tags=["usuarios"])
app.include_router(servicio_rotuer, tags=["servicios"])
app.include_router(pago_router,tags=["pagos"] )
app.include_router(factura_router, tags=["facturas"])

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



# Rutas de la API

@app.get("/")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/signup")
async def get_signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

#health check
@app.get("/health")
async def health():
    return JSONResponse(content={"message": "Healthy"}, status_code=200)


