from fastapi import APIRouter
from app.schemas.server import ServerCreate

router = APIRouter(prefix="/servers", tags=["Servers"])

servers = []

@router.post("/")
def create_server(server: ServerCreate):
    servers.append(server)
    return server

@router.get("/")
def get_servers():
    return servers