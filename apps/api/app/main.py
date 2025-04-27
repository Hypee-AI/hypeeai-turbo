from fastapi import FastAPI
from app.api.v1.routes.ping import router as ping_router

app = FastAPI()

app.include_router(ping_router, prefix="/v1/ping")

@app.get("/")
async def root():
    return {"message": "API is running"}
