from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.user_model import User
from models.doctor_application_model import DoctorApplication
from models.contact_model import ContactQuery

router = APIRouter(prefix="/admin", tags=["Admin"])

# 1) Get All Users


@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):

    users = db.query(User).all()
    return users


# 2) Get All Doctor Application


@router.get("/doctor-applications")
def get_doctor_applications(db: Session = Depends(get_db)):

    applications = db.query(DoctorApplication).all()
    return applications


# 3) Approve Doctor


@router.put("/approve-doctor/{doctor_id}")
def approve_doctor(doctor_id: int, db: Session = Depends(get_db)):

    doctor = db.query(User).filter(User.id == doctor_id).first()

    if not doctor:
        return {"error": "Doctor not found"}

    doctor.role = "doctor"

    db.commit()

    return {"message": "Doctor approved successfully"}


# 5) Get Contact Queries (Admin)


@router.get("/contact-queries")
def get_contact_queries(db: Session = Depends(get_db)):

    queries = db.query(ContactQuery).all()
    return queries


# 6) Delete User


@router.delete("/delete-user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"error": "User not found"}

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}
