import geopandas as gpd

from rasterio.mask import mask
from app.core.logger import logger

def clip_to_district(
    raster,
    geojson_path,
    district_name
):
    try:
        logger.info(
            f"Clipping raster to district: {district_name}"
        )

        districts = gpd.read_file(
                geojson_path
            )

        district = districts[
                districts["name"]
                ==
                district_name
            ]

        geometry = district.geometry.values

        clipped,transform = mask(
            raster,
            geometry,
            crop=True
        )

        return clipped

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "District clipping failed"
        )