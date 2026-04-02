from pydantic import BaseModel
from datetime import datetime

class MetricCreate(BaseModel):
    cpu: float
    ram: float
    disk: float
    server_id: int

class MetricResponse(MetricCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True