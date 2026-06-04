from app.core.logger import logger

def calculate_weather_score(
    rainfall,
    humidity,
    temperature
):
    try:
        logger.info(
            "Calculating weather score..."
        )

        score = (
            rainfall * 0.3
            +
            humidity * 0.3
            +
            temperature * 0.4
        )

        return score

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Weather utility failed"
        )