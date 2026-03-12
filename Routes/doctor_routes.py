from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.doctor_model import Doctor
from schemas.doctor_schema import DoctorCreate

router = APIRouter(prefix="/doctors", tags=["Doctors"])


# Create Doctor
@router.post("/")
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):

    new_doctor = Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        experience=doctor.experience,
        hospital=doctor.hospital,
    )

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return new_doctor


# Get All Doctors
@router.get("/")
def get_doctors(db: Session = Depends(get_db)):

    doctors = db.query(Doctor).all()

    return doctors


# Get Doctor By ID
@router.get("/{doctor_id}")
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):

    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


# Update Doctor
@router.put("/{doctor_id}")
def update_doctor(
    doctor_id: int, updated_doctor: DoctorCreate, db: Session = Depends(get_db)
):

    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor.name = updated_doctor.name
    doctor.specialization = updated_doctor.specialization
    doctor.experience = updated_doctor.experience
    doctor.hospital = updated_doctor.hospital

    db.commit()
    db.refresh(doctor)

    return doctor


# Delete Doctor
@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):

    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    db.delete(doctor)
    db.commit()

    return {"message": "Doctor deleted successfully"}
