from sqlalchemy import Column, Integer, ForeignKey, Date
from database import Base


class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("users.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    appointment_date = Column(Date)
