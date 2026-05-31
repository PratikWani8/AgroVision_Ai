from app.core.logger import logger

def crop_stress_analysis(
    ndvi,
    ndwi,
    temperature
):
    try:
        logger.info(
            "Running crop stress analysis..."
        )

        stress_score = (
            (1 - ndvi) * 40
            +
            (1 - ndwi) * 40
            +
            temperature * 0.2
        )

        level = "LOW"

        if stress_score > 70:
            level = "HIGH"

        elif stress_score > 40:
            level = "MEDIUM"

        return {
            "stress_score":
                stress_score,

            "stress_level":
                level
        }

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Crop stress analysis failed"
        )