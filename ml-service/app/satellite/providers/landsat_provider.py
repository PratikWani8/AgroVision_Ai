from app.core.logger import logger

class LandsatProvider:

    BASE_URL = (
        "https://landsatlook.usgs.gov"
    )

    def fetch_metadata(
        self,
        latitude,
        longitude
    ):
        try:
            logger.info(
                f"Fetching Landsat metadata for "
                f"{latitude}, {longitude}"
            )

            return {
                "status": "success",
                "provider": "Landsat",
                "latitude": latitude,
                "longitude": longitude,
                "message": (
                    "Landsat integration "
                    "not implemented yet"
                )
            }

        except Exception as e:
            logger.error(str(e))

            raise Exception(
                "Failed to fetch Landsat metadata"
            )