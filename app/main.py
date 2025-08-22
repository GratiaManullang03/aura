from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.api import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    openapi_url=f"/openapi.json" if settings.DEBUG else None
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure sesuai kebutuhan
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
    """
    Endpoint selamat datang untuk root URL.
    Memberikan informasi dasar tentang API.
    """
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "docs_url": "/docs",
    }

# Include routers
app.include_router(api_router, prefix="/api/v1")