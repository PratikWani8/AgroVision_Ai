from fastapi import APIRouter

from app.api.routes.health import ( router as health_router )

from app.api.routes.prediction import ( router as prediction_router )

from app.api.routes.training import ( router as training_router )

from app.api.routes.district_risk import ( router as district_risk_router )

from app.api.routes.satellite import ( router as satellite_router )

from app.api.routes.analytics import ( router as analytics_router )

from app.api.routes.weather import ( router as weather_router )

from app.api.routes.alerts import ( router as alerts_router )

api_router = APIRouter(
    prefix="/api/v1"
)

api_router.include_router(
    health_router,
    tags=["Health"]
)

api_router.include_router(
    prediction_router,
    tags=["Prediction"]
)

api_router.include_router(
    training_router,
    tags=["Training"]
)

api_router.include_router(
    district_risk_router,
    tags=["District Risk"]
)

api_router.include_router(
    satellite_router,
    tags=["Satellite Intelligence"]
)

api_router.include_router(
    analytics_router,
    tags=["Analytics"]
)

api_router.include_router(
    weather_router,
    tags=["Weather Intelligence"]
)

api_router.include_router(
    alerts_router,
    tags=["Alert System"]
)