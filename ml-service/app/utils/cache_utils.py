from app.core.logger import logger

CACHE = {}

def set_cache(
    key,
    value
):
    try:
        logger.info(
            f"Setting cache: {key}"
        )

        CACHE[key] = value

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Cache set failed"
        )

def get_cache(
    key
):
    try:
        logger.info(
            f"Fetching cache: {key}"
        )

        return CACHE.get(key)

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Cache fetch failed"
        )