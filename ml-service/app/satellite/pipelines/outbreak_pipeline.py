from app.core.logger import logger
from app.satellite.analytics.outbreak_analysis import ( outbreak_analysis )

def outbreak_pipeline(
    ndvi,
    humidity,
    temperature
):
    try:
        logger.info(
            "Running outbreak pipeline..."
        )

        result = outbreak_analysis(
                ndvi,
                humidity,
                temperature
            )

        return result

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Outbreak pipeline failed"
        )