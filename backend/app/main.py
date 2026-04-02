from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import servers
from app.routes import metrics
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Server Monitoring Platform")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción se restringe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(servers.router)
app.include_router(metrics.router)

@app.get("/")
def root():
    return {"status": "running"}