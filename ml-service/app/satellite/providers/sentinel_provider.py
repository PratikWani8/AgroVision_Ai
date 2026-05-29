from sentinelhub import (
    SHConfig,
    SentinelHubRequest,
    DataCollection,
    MimeType,
    CRS,
    BBox
)

from app.core.logger import logger
from app.core.config import settings

class SentinelProvider:

    def __init__(self):
        self.config = SHConfig()

        self.config.sh_client_id = (
            settings.SENTINEL_CLIENT_ID
        )

        self.config.sh_client_secret = (
            settings.SENTINEL_CLIENT_SECRET
        )

    def fetch_imagery(
        self,
        bbox_coords,
        time_interval
    ):
        try:
            logger.info(
                "Fetching Sentinel-2 imagery..."
            )

            bbox = BBox(
                bbox=bbox_coords,
                crs=CRS.WGS84
            )

            evalscript = """
            //VERSION=3

            function setup() {
              return {
                input: [{
                  bands: ["B02", "B03", "B04", "B08"]
                }],
                output: {
                  bands: 4
                }
              };
            }

            function evaluatePixel(sample) {
              return [
                sample.B02,
                sample.B03,
                sample.B04,
                sample.B08
              ];
            }
            """

            request = SentinelHubRequest(
                    evalscript=evalscript,

                    input_data=[
                        SentinelHubRequest.input_data(
                            data_collection=
                            DataCollection.SENTINEL2_L2A,

                            time_interval=
                            time_interval
                        )
                    ],

                    responses=[
                        SentinelHubRequest.output_response(
                            "default",
                            MimeType.TIFF
                        )
                    ],

                    bbox=bbox,

                    size=(512, 512),

                    config=self.config
                )

            data = request.get_data()

            logger.info(
                "Sentinel imagery fetched successfully"
            )

            return data

        except Exception as e:
            logger.error(str(e))

            raise Exception(
                "Failed to fetch Sentinel imagery"
            )