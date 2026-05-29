import numpy as np

from app.core.logger import logger

def calculate_savi(
    nir_band,
    red_band,
    L=0.5
):
    try:
        logger.info(
            "Calculating SAVI..."
        )

        np.seterr(
            divide="ignore",
            invalid="ignore"
        )

        savi = (
            (
                nir_band - red_band
            )
            /
            (
                nir_band
                + red_band
                + L
            )
        ) * (1 + L)

        return savi

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "SAVI calculation failed"
        )