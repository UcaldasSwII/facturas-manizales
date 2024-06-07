from config.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)  # Agregar el campo 'name'
    password = Column(String)  # Campo 'hashed_password' definido correctamente

    servicios = relationship("Servicio", back_populates="usuario")