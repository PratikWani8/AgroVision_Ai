import os

from app.core.logger import logger

def get_environment():
    try:
        logger.info(
            "Fetching environment..."
        )

        return os.getenv(
            "ENV",
            "development"
        )

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Environment fetch failed"
        )