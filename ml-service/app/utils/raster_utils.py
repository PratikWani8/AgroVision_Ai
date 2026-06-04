import numpy as np

from app.core.logger import logger

def normalize_raster(
    raster
):
    try:
        logger.info(
            "Normalizing raster..."
        )

        normalized = (
            raster - np.min(raster)
        ) / (
            np.max(raster)
            -
            np.min(raster)
        )

        return normalized

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Raster normalization failed"
        )