from app.core.logger import logger
from app.satellite.processing.district_clipper import ( clip_to_district)

def district_processing_pipeline(
    raster,
    geojson_path,
    district_name
):
    try:
        logger.info(
            f"Running district pipeline for {district_name}"
        )

        clipped = clip_to_district(
                raster,
                geojson_path,
                district_name
            )

        return clipped

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "District pipeline failed"
        )