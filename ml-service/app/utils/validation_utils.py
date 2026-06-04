from app.core.logger import logger

def validate_coordinates(
    latitude,
    longitude
):
    try:
        logger.info(
            "Validating coordinates..."
        )

        if latitude < -90 or latitude > 90:
            return False

        if longitude < -180 or longitude > 180:
            return False

        return True

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Coordinate validation failed"
        )