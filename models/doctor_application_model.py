from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class DoctorApplication(Base):

    __tablename__ = "doctor_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    specialization = Column(String(100))
    experience = Column(Integer)
    certificate = Column(String(200))
    status = Column(String(50), default="PENDING")
