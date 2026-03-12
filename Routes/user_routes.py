from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies import get_current_user
from models.user_model import User
from schemas.user_schema import UserProfile, UpdateProfile

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/profile", response_model=UserProfile)
def get_profile(
    db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)
):

    user = db.query(User).filter(User.id == current_user["user_id"]).first()

    return user


@router.put("/profile")
def update_profile(
    profile: UpdateProfile,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):

    user = db.query(User).filter(User.id == current_user["user_id"]).first()

    for key, value in profile.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()

    return {"message": "Profile updated successfully"}
