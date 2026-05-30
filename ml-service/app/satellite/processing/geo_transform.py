from app.core.logger import logger

def get_geo_transform(
    dataset
):
    try:
        logger.info(
            "Extracting geo transform..."
        )

        return dataset.transform

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Geo transform extraction failed"
        )