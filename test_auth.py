from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.db import Base, get_db
from main import app


SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
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

def test_register_user():
    response = client.post(
        "/users/",
        json={
            "id": 1,
            "username": "yo",
            "email": "yo@mail.com",
            "name": "yo",
            "password": "123"
    })
    assert response.status_code == 201
    assert response.json()['message'] == 'User created'

def test_login_user():
    response = client.post(
        "/auth/login",
        json={
            "username": "yo",
            "password": "123"
    })
    assert response.status_code == 200
    assert 'token' in response.json()

def test_get_all_users():
    response = client.get(
        "/users/",
    )
    assert response.status_code == 200
    assert len(response.json()) > 0





