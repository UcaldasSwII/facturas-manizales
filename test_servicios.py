"""
Test file for pytest to test the module Servicios that have a model with:
    codigo_suscripcion = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    tipo = Column(Enum(ListaServicios))
    usuario_id = Column(Integer, ForeignKey('users.id'))
"""
from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.db import Base, get_db
from main import app


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_servicio():
    response = client.post(
        "/servicios/",
        json={"codigo_suscripcion": 112, "nombre": "Servicio 1", "tipo": "AGUAS DE MANIZALES", "usuario_id": 1},
    )
    assert response.status_code == 201
    assert response.json() == {"message": "Servicio creado"}
