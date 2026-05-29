import numpy as np

from app.core.logger import logger

def calculate_gndvi(
    nir_band,
    green_band
):
    try:
        logger.info(
            "Calculating GNDVI..."
        )

        np.seterr(
            divide="ignore",
            invalid="ignore"
        )

        gndvi = (
            nir_band - green_band
        ) / (
            nir_band + green_band
        )

        return gndvi

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "GNDVI calculation failed"
        )