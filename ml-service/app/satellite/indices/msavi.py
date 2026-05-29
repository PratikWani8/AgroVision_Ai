import numpy as np

from app.core.logger import logger

def calculate_msavi(
    nir_band,
    red_band
):
    try:
        logger.info(
            "Calculating MSAVI..."
        )

        np.seterr(
            divide="ignore",
            invalid="ignore"
        )

        msavi = (
            (
                2 * nir_band
                + 1
            )
            -
            np.sqrt(
                (
                    2 * nir_band + 1
                ) ** 2
                -
                8 * (
                    nir_band
                    - red_band
                )
            )
        ) / 2

        return msavi

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "MSAVI calculation failed"
        )