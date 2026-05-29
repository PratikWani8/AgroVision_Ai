from app.core.logger import logger

class NASAProvider:

    NASA_EARTHDATA_URL = (
        "https://earthdata.nasa.gov"
    )

    def fetch_data(
        self,
        latitude,
        longitude
    ):
        try:
            logger.info(
                f"Fetching NASA data for "
                f"{latitude}, {longitude}"
            )

            return {
                "status": "success",
                "provider": "NASA",
                "latitude": latitude,
                "longitude": longitude,
                "message": (
                    "NASA integration "
                    "not implemented"
                )
            }

        except Exception as e:
            logger.error(str(e))

            raise Exception(
                "NASA EarthData fetch failed"
            )