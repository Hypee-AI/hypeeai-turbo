from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.ping import router as ping_router
from app.routes.auth import router as auth_router
from app.routes.facebook import router as facebook_router
from app.core.config import settings

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ping_router, prefix=f"/api/{settings.api_version}")
app.include_router(auth_router, prefix=f"/api/{settings.api_version}")
app.include_router(facebook_router, prefix=f"/api/{settings.api_version}")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": f"{settings.app_name} is running",
        "version": settings.api_version,
        "docs": "/docs"
    }
