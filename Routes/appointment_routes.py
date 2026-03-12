from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_current_user
from database import get_db
from models.appointment_model import Appointment
from schemas.appointment_schema import AppointmentCreate

router = APIRouter(prefix="/appointments", tags=["Appointments"])


# Book Appointment
@router.post("/")
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):

    if current_user["role"] != "PATIENT":
        raise HTTPException(
            status_code=403, detail="Only patients can book appointments"
        )

    new_appointment = Appointment(
        patient_id=current_user["user_id"],
        doctor_id=appointment.doctor_id,
        appointment_date=appointment.appointment_date,
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment


# Get All Appointments
@router.get("/")
def get_appointments(db: Session = Depends(get_db)):

    appointments = db.query(Appointment).all()

    return appointments


# Get My Appointments
@router.get("/patient/{patient_id}")
def get_patient_appointments(patient_id: int, db: Session = Depends(get_db)):

    appointments = (
        db.query(Appointment).filter(Appointment.patient_id == patient_id).all()
    )

    return appointments


# Cancel Appointment
@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):

    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    db.delete(appointment)
    db.commit()

    return {"message": "Appointment cancelled successfully"}
