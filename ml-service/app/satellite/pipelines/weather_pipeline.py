from app.core.logger import logger

def weather_pipeline(
    rainfall,
    humidity,
    temperature
):
    try:
        logger.info(
            "Running weather intelligence pipeline..."
        )

        weather_score = (
            rainfall * 0.3
            +
            humidity * 0.3
            +
            temperature * 0.4
        )

        return {
            "weather_score":
                weather_score
        }

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Weather pipeline failed"
        )