from fastapi import APIRouter
from schemas import Driver
from database import drivers

router = APIRouter()

@router.post("/")
def create_driver(driver: Driver):
    drivers.append(driver)
    return driver

@router.get("/")
def list_drivers():
    return drivers