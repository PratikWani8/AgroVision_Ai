from app.core.logger import logger

def engineer_features(
    dataframe
):
    try:
        logger.info(
            "Engineering features..."
        )

        dataframe[
            "vegetation_health"
        ] = (
            dataframe["ndvi"]
            *
            dataframe["humidity"]
        )

        return dataframe

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Feature engineering failed"
        )