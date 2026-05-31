import numpy as np

from app.core.logger import logger

def detect_drought(
    ndvi_array,
    rainfall_array
):
    try:
        logger.info(
            "Running drought detection..."
        )

        drought_score = (
            (1 - np.nanmean(ndvi_array))
            *
            np.nanmean(rainfall_array)
        )

        severity = "LOW"

        if drought_score > 50:
            severity = "HIGH"

        elif drought_score > 25:
            severity = "MEDIUM"

        return {
            "drought_score":
                float(drought_score),

            "severity":
                severity
        }

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Drought detection failed"
        )