import numpy as np

from app.core.logger import logger

def vegetation_trend(
    historical_ndvi
):
    try:
        logger.info(
            "Analyzing vegetation trend..."
        )

        trend = np.polyfit(
            range(len(historical_ndvi)),
            historical_ndvi,
            1
        )[0]

        direction = "STABLE"

        if trend > 0:
            direction = "INCREASING"

        elif trend < 0:
            direction = "DECREASING"

        return {
            "trend":
                float(trend),

            "direction":
                direction
        }

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Vegetation trend analysis failed"
        )