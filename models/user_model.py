from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(200))
    role = Column(String(50))
    phone = Column(String(50))
    age = Column(Integer)
    gender = Column(String(25))
    address = Column(String(100))
