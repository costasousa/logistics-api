from fastapi import APIRouter, HTTPException
from schemas import Delivery, DeliveryStatus
from database import deliveries

router = APIRouter()

@router.post("/")
def create_delivery(delivery: Delivery):
    deliveries.append(delivery)
    return delivery

@router.get("/")
def list_deliveries(status: DeliveryStatus = None):
    if status:
        return [d for d in deliveries if d.status == status]
    return deliveries

@router.put("/{delivery_id}/assign/{driver_id}")
def assign_driver(delivery_id: int, driver_id: int):
    for d in deliveries:
        if d.id == delivery_id:
            d.assigned_driver_id = driver_id
            return d
    raise HTTPException(status_code=404, detail="Delivery not found")

@router.put("/{delivery_id}/status/{status}")
def update_status(delivery_id: int, status: DeliveryStatus):
    for d in deliveries:
        if d.id == delivery_id:
            d.status = status
            return d
    raise HTTPException(status_code=404, detail="Delivery not found")