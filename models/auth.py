from config.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    