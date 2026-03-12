from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.contact_model import ContactQuery
from schemas.contact_schema import ContactCreate

router = APIRouter(prefix="/contact", tags=["Contact"])


@router.post("/send")
def send_query(query: ContactCreate, db: Session = Depends(get_db)):

    new_query = ContactQuery(name=query.name, email=query.email, message=query.message)

    db.add(new_query)
    db.commit()
    db.refresh(new_query)

    return {"message": "Query sent successfully"}
