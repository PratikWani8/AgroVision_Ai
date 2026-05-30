import rasterio

from rasterio.transform import from_origin
from app.core.logger import logger

def export_tif(
    data,
    output_path
):
    try:
        logger.info(
            "Exporting GeoTIFF..."
        )

        height, width = data.shape

        transform = from_origin(
                0,
                0,
                1,
                1
            )

        with rasterio.open(
            output_path,
            "w",
            driver="GTiff",
            height=height,
            width=width,
            count=1,
            dtype=data.dtype,
            crs="+proj=latlong",
            transform=transform
        ) as dst:

            dst.write(data, 1)

        return output_path

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "GeoTIFF export failed"
        )