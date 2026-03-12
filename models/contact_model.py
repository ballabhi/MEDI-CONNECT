from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime


class ContactQuery(Base):
    __tablename__ = "contact_queries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    message = Column(String(500))
    created_at = Column(DateTime, default=datetime.now)
