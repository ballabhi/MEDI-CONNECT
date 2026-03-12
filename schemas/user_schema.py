from pydantic import BaseModel, EmailStr
from typing import Optional


class UserRegister(BaseModel):
    name: str
    email: str
    password: str
    role: str
    phone: str
    age: int
    gender: str
    address: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True


class UserProfile(BaseModel):
    name: str
    email: str
    phone: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    address: Optional[str]

    class Config:
        from_attributes = True


class UpdateProfile(BaseModel):
    phone: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    address: Optional[str]
