from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from app.db.schemas import DeliveryStatus


DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DriverDB(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    vehicle_plate = Column(String)

class DeliveryDB(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    package = Column(String)
    destination = Column(String)
    status = Column(Enum(DeliveryStatus), default=DeliveryStatus.PENDING)
    assigned_driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=True)

    driver = relationship("DriverDB")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()