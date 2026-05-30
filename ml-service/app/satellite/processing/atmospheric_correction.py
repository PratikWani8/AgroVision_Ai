from app.core.logger import logger

def atmospheric_correction(
    raster
):
    try:
        logger.info(
            "Applying atmospheric correction..."
        )

        corrected = raster

        return corrected

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Atmospheric correction failed"
        )