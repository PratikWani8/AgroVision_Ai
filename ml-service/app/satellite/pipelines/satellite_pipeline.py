from app.core.logger import logger
from app.satellite.processing.raster_loader import ( load_raster )
from app.satellite.processing.band_extractor import ( extract_band )
from app.satellite.indices.ndvi import ( calculate_ndvi )
from app.satellite.indices.ndwi import ( calculate_ndwi )
from app.satellite.indices.evi import ( calculate_evi )
from app.satellite.indices.vegetation_stats import ( vegetation_statistics )

def process_satellite_image(
    image_path
):
    try:
        logger.info(
            "Starting satellite processing pipeline..."
        )

        dataset = load_raster(
            image_path
        )

        red = extract_band(
            dataset,
            4
        )

        green = extract_band(
            dataset,
            3
        )

        blue = extract_band(
            dataset,
            2
        )

        nir = extract_band(
            dataset,
            8
        )

        ndvi = calculate_ndvi(
            nir,
            red
        )

        ndwi = calculate_ndwi(
            green,
            nir
        )

        evi = calculate_evi(
            nir,
            red,
            blue
        )

        return {
            "ndvi":
                vegetation_statistics(
                    ndvi
                ),

            "ndwi":
                vegetation_statistics(
                    ndwi
                ),

            "evi":
                vegetation_statistics(
                    evi
                )
        }

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Satellite pipeline failed"
        )