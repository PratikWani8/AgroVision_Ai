import geopandas as gpd

from app.core.logger import logger

def export_geojson(
    geodataframe,
    output_path
):
    try:
        logger.info(
            "Exporting GeoJSON..."
        )

        geodataframe.to_file(
            output_path,
            driver="GeoJSON"
        )

        return output_path

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "GeoJSON export failed"
        )