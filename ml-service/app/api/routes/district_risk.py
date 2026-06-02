from fastapi import APIRouter

from app.satellite.analytics.risk_scoring import ( calculate_risk_score )

from app.core.logger import logger

router = APIRouter()

@router.post("/district-risk")
def district_risk(
    payload: dict
):
    try:
        logger.info(
            "District risk API called"
        )

        result = calculate_risk_score(
            payload["ndvi"],
            payload["humidity"],
            payload["rainfall"],
            payload["temperature"]
        )

        return {
            "success": True,

            "data": result
        }

    except Exception as e:
        logger.error(str(e))

        return {
            "success": False,

            "message": str(e)
        }