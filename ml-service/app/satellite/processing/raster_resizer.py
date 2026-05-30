from app.core.logger import logger

def resize_raster(
    raster,
    width,
    height
):
    try:
        logger.info(
            f"Resizing raster to {width}x{height}"
        )

        resized = raster.read(
            out_shape=(
                raster.count,
                height,
                width
            )
        )

        return resized

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Raster resizing failed"
        )