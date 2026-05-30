from rasterio.warp import (
    calculate_default_transform,
    reproject,
    Resampling
)

from app.core.logger import logger

def reproject_raster(
    source,
    destination_crs
):
    try:
        logger.info(
            "Reprojecting raster..."
        )

        transform, width, height = (
            calculate_default_transform(
                source.crs,
                destination_crs,
                source.width,
                source.height,
                *source.bounds
            )
        )

        return {
            "transform":
                transform,

            "width":
                width,

            "height":
                height
        }

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Raster reprojection failed"
        )