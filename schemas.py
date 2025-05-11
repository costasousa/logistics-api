from pydantic import BaseModel
from typing import Optional
from enum import Enum

class DeliveryStatus(str, Enum):
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"

class Driver(BaseModel):
    id: int
    name: str
    vehicle_plate: str

class Delivery(BaseModel):
    id: int
    package: str
    destination: str
    status: DeliveryStatus = DeliveryStatus.PENDING
    assigned_driver_id: Optional[int] = None