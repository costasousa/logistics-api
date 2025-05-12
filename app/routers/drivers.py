from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db, DriverDB
from app.db.schemas import Driver, DriverCreate

router = APIRouter()

@router.post("/", response_model=Driver)
def create_driver(driver: DriverCreate, db: Session = Depends(get_db)):

    db_driver = DriverDB(**driver.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    
    return db_driver

@router.get("/", response_model=list[Driver])
def list_drivers(db: Session = Depends(get_db)):

    return db.query(DriverDB).all()