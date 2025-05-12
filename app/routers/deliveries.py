from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db, DeliveryDB
from app.db.schemas import Delivery, DeliveryCreate, DeliveryStatus

router = APIRouter()

@router.post("/", response_model=Delivery)
def create_delivery(delivery: DeliveryCreate, db: Session = Depends(get_db)):

    db_delivery = DeliveryDB(**delivery.dict(), status=DeliveryStatus.PENDING)
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery

@router.get("/", response_model=list[Delivery])
def list_deliveries(status: DeliveryStatus = None, db: Session = Depends(get_db)):

    query = db.query(DeliveryDB)

    if status:
        query = query.filter(DeliveryDB.status == status)

    return query.all()

@router.put("/{delivery_id}/assign/{driver_id}", response_model=Delivery)
def assign_driver(delivery_id: int, driver_id: int, db: Session = Depends(get_db)):

    delivery = db.query(DeliveryDB).filter(DeliveryDB.id == delivery_id).first()

    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    
    delivery.assigned_driver_id = driver_id
    db.commit()
    db.refresh(delivery)

    return delivery

@router.put("/{delivery_id}/status/{status}", response_model=Delivery)
def update_status(delivery_id: int, status: DeliveryStatus, db: Session = Depends(get_db)):

    delivery = db.query(DeliveryDB).filter(DeliveryDB.id == delivery_id).first()

    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    
    delivery.status = status
    db.commit()
    db.refresh(delivery)
    
    return delivery