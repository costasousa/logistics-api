from fastapi import FastAPI
from routers import deliveries, drivers

app = FastAPI(title="Logistic API")

app.include_router(drivers.router, prefix="/drivers", tags=["Drivers"])
app.include_router(deliveries.router, prefix="/deliveries", tags=["Deliveries"])