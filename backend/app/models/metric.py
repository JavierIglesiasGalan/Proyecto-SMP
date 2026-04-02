from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from datetime import datetime
from app.core.database import Base

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    cpu = Column(Float)
    ram = Column(Float)
    disk = Column(Float)

    timestamp = Column(DateTime, default=datetime.utcnow)

    server_id = Column(Integer, ForeignKey("servers.id"))