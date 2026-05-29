import numpy as np

from app.core.logger import logger

def calculate_evi(
    nir_band,
    red_band,
    blue_band
):
    try:
        logger.info(
            "Calculating EVI..."
        )

        np.seterr(
            divide="ignore",
            invalid="ignore"
        )

        evi = 2.5 * (
            (
                nir_band - red_band
            )
            /
            (
                nir_band
                + 6 * red_band
                - 7.5 * blue_band
                + 1
            )
        )

        return evi

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "EVI calculation failed"
        )