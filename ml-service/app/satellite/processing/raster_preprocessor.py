from app.core.logger import logger

def preprocess_raster(dataset):
    try:
        logger.info(
            "Preprocessing raster..."
        )

        return dataset

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Raster preprocessing failed"
        ) 