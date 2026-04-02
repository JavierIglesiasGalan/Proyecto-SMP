from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.server import Server
from app.schemas.server import ServerCreate, ServerResponse
from app.models.metric import Metric

router = APIRouter(prefix="/servers", tags=["Servers"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ServerResponse)
def create_server(server: ServerCreate, db: Session = Depends(get_db)):
    db_server = Server(name=server.name, ip=server.ip)
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server

@router.get("/", response_model=list[ServerResponse])
def get_servers(db: Session = Depends(get_db)):
    return db.query(Server).all()
@router.get("/{server_id}/metrics")
def get_server_metrics(server_id: int, db: Session = Depends(get_db)):
    return db.query(Metric).filter(Metric.server_id == server_id).all()
@router.get("/{server_id}/metrics/latest")
def get_latest_metric(server_id: int, db: Session = Depends(get_db)):
    return (
        db.query(Metric)
        .filter(Metric.server_id == server_id)
        .order_by(Metric.timestamp.desc())
        .first()
    )