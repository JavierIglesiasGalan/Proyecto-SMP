from fastapi import FastAPI
from app.routes import users, servers, metrics

app = FastAPI(title="Server Monitoring API")

app.include_router(users.router)
app.include_router(servers.router)
app.include_router(metrics.router)

@app.get("/")
def root():
    return {"message": "API running"}