from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.metric import Metric
from app.schemas.metric import MetricCreate, MetricResponse

router = APIRouter(prefix="/metrics", tags=["Metrics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MetricResponse)
def create_metric(metric: MetricCreate, db: Session = Depends(get_db)):
    db_metric = Metric(**metric.dict())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

@router.get("/")
def get_metrics(db: Session = Depends(get_db)):
    return db.query(Metric).all()