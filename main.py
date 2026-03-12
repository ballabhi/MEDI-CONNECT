from fastapi import FastAPI
from database import engine, Base


from Routes import auth_routes
from Routes import doctor_routes
from Routes import appointment_routes
from Routes import user_routes
from Routes import doctor_application_routes
from Routes import contact_routes
from Routes import admin_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(doctor_routes.router)
app.include_router(appointment_routes.router)
app.include_router(user_routes.router)
app.include_router(doctor_application_routes.router)
app.include_router(contact_routes.router)
app.include_router(admin_routes.router)


@app.get("/")
def home():
    return {"message": "Medical Appointment Booking API Running"}
