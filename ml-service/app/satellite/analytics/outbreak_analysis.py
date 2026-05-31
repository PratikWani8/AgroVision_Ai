from app.core.logger import logger

def outbreak_analysis(
    ndvi,
    humidity,
    temperature
):
    try:
        logger.info(
            "Running outbreak analysis..."
        )

        score = (
            (1 - ndvi) * 50
            +
            humidity * 0.3
            +
            temperature * 0.2
        )

        risk = "LOW"

        if score > 70:
            risk = "HIGH"

        elif score > 40:
            risk = "MEDIUM"

        return {
            "outbreak_score":
                score,

            "risk":
                risk
        }

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Outbreak analysis failed"
        )