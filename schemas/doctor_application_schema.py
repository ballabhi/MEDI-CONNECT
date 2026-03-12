from pydantic import BaseModel


class DoctorApplicationCreate(BaseModel):

    specialization: str
    experience: int
    certificate: str
