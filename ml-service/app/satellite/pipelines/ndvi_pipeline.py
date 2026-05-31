from app.core.logger import logger
from app.satellite.indices.ndvi import ( calculate_ndvi )
from app.satellite.indices.vegetation_stats import ( vegetation_statistics )

def run_ndvi_pipeline(
    nir_band,
    red_band
):
    try:
        logger.info(
            "Running NDVI pipeline..."
        )

        ndvi = calculate_ndvi(
            nir_band,
            red_band
        )

        stats = vegetation_statistics(
                ndvi
            )

        return stats

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "NDVI pipeline failed"
        )