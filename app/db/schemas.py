from pydantic import BaseModel
from typing import Optional
from enum import Enum

class DeliveryStatus(str, Enum):
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"

class DriverBase(BaseModel):
    name: str
    vehicle_plate: str

class DriverCreate(DriverBase):
    pass

class Driver(DriverBase):
    id: int

    class Config:
        orm_mode = True

class DeliveryBase(BaseModel):
    package: str
    destination: str

class DeliveryCreate(DeliveryBase):
    pass

class Delivery(DeliveryBase):
    id: int
    status: DeliveryStatus = DeliveryStatus.PENDING
    assigned_driver_id: Optional[int] = None

    class Config:
        orm_mode = True