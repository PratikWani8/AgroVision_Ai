import numpy as np

from app.core.logger import logger

def calculate_ndwi(
    green_band,
    nir_band
):
    try:
        logger.info(
            "Calculating NDWI..."
        )

        np.seterr(
            divide="ignore",
            invalid="ignore"
        )

        ndwi = (
            green_band - nir_band
        ) / (
            green_band + nir_band
        )

        return ndwi

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "NDWI calculation failed"
        )