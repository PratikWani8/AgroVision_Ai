from fastapi import APIRouter

from app.satellite.analytics.outbreak_analysis import ( outbreak_analysis )

from app.satellite.analytics.crop_stress_analysis import ( crop_stress_analysis )

from app.core.logger import logger

router = APIRouter()

@router.post("/analytics")
def analytics(
    payload: dict
):
    try:
        logger.info(
            "Analytics API called"
        )

        outbreak = outbreak_analysis(
                payload["ndvi"],
                payload["humidity"],
                payload["temperature"]
            )

        stress = crop_stress_analysis(
                payload["ndvi"],
                payload["ndwi"],
                payload["temperature"]
            )

        return {
            "success": True,

            "outbreak":
                outbreak,

            "stress":
                stress
        }

    except Exception as e:
        logger.error(str(e))

        return {
            "success": False,

            "message": str(e)
        }