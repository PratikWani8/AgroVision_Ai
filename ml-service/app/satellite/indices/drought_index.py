import numpy as np

from app.core.logger import logger

def calculate_drought_index(
    ndvi,
    temperature
):
    try:
        logger.info(
            "Calculating drought index..."
        )

        drought = (
            1 - ndvi
        ) * temperature

        return drought

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Drought index calculation failed"
        )