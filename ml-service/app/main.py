from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api import api_router

from app.core.logger import logger

from app.core.middleware import ( log_requests )

app = FastAPI(
    title="AgroVision AI ML Service",

    description=(
        "Production-grade Geospatial AI "
        "Microservice for Crop Disease "
        "Detection using Satellite Imagery"
    ),

    version="1.0.0"
)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

app.middleware("http")(
    log_requests
)

app.include_router(api_router)

@app.get("/")
def root():
    return {
        "success": True,

        "service":
            "AgroVision AI ML Service",

        "status":
            "running",

        "version":
            "1.0.0"
    }

@app.on_event("startup")
async def startup_event():
    logger.info(
        "AgroVision ML Service Started"
    )

@app.on_event("shutdown")
async def shutdown_event():
    logger.info(
        "AgroVision ML Service Stopped"
    )