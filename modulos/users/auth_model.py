from sqlalchemy import Column, Integer, String
<<<<<<<< HEAD:modulos/users/users_model.py
from sqlalchemy.orm import Session, relationship
from passlib.hash import bcrypt
from config.db import Base
========
from sqlalchemy.orm import relationship
>>>>>>>> master:modulos/users/auth_model.py

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
<<<<<<<< HEAD:modulos/users/users_model.py
    hashed_password = Column(String)




========
    name = Column(String)  # Agregar el campo 'name'
    password = Column(String)  # Campo 'hashed_password' definido correctamente

    servicios = relationship("Servicio", back_populates="usuario")
>>>>>>>> master:modulos/users/auth_model.py
