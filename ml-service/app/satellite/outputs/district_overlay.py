import geopandas as gpd
import matplotlib.pyplot as plt

from app.core.logger import logger

def generate_district_overlay(
    geojson_path,
    output_path
):
    try:
        logger.info(
            "Generating district overlay..."
        )

        gdf = gpd.read_file(
                geojson_path
            )

        gdf.plot()

        plt.savefig(output_path)

        plt.close()

        return output_path

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "District overlay generation failed"
        )