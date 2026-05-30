from app.core.logger import logger

def generate_analytics_report(
    analytics
):
    try:
        logger.info(
            "Generating analytics report..."
        )

        report = {
            "summary":
                "Crop intelligence analytics generated successfully.",

            "analytics":
                analytics
        }

        return report

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Analytics report generation failed"
        )