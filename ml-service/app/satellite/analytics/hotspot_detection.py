from app.core.logger import logger

def detect_hotspots(
    district_data
):
    try:
        logger.info(
            "Detecting outbreak hotspots..."
        )

        hotspots = []

        for district in district_data:
            if district["risk"] > 70:
                hotspots.append(
                    district
                )

        return {
            "hotspots":
                hotspots,

            "count":
                len(hotspots)
        }

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Hotspot detection failed"
        )