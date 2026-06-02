from fastapi import APIRouter

from app.core.logger import logger

router = APIRouter()

@router.post("/alerts/generate")
def generate_alert(
    payload: dict
):
    try:
        logger.info(
            "Alert generation API called"
        )

        if payload["risk"] > 70:
            severity = "HIGH"

        elif payload["risk"] > 40:
            severity = "MEDIUM"

        else:
            severity = "LOW"

        return {
            "success": True,

            "alert": {
                "severity":
                    severity,

                "message":
                    "Potential disease outbreak detected"
            }
        }

    except Exception as e:
        logger.error(str(e))

        return {
            "success": False,

            "message": str(e)
        }