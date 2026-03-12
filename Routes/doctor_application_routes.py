from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from dependencies import get_current_user
from models.doctor_application_model import DoctorApplication
from schemas.doctor_application_schema import DoctorApplicationCreate

router = APIRouter(prefix="/doctor", tags=["Doctor Application"])

# Apply to Become Doctor


@router.post("/apply")
def apply_doctor(
    application: DoctorApplicationCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):

    new_application = DoctorApplication(
        user_id=current_user["user_id"],
        specialization=application.specialization,
        experience=application.experience,
        certificate=application.certificate,
        status="PENDING",
    )

    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return {"message": "Application submitted successfully"}


@router.get("/applications")
def get_applications(
    db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)
):

    if current_user["role"] != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin only")

    applications = db.query(DoctorApplication).all()

    return applications


@router.put("/applications/{id}/approve")
def approve_application(
    id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):

    if current_user["role"] != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin only")

    application = db.query(DoctorApplication).filter(DoctorApplication.id == id).first()

    application.status = "APPROVED"

    db.commit()

    return {"message": "Doctor application approved"}
