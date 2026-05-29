import numpy as np

from app.core.logger import logger

def vegetation_statistics(
    index_array
):
    try:
        logger.info(
            "Generating vegetation statistics..."
        )

        stats = {
            "mean": float(
                np.nanmean(
                    index_array
                )
            ),

            "min": float(
                np.nanmin(
                    index_array
                )
            ),

            "max": float(
                np.nanmax(
                    index_array
                )
            ),

            "std": float(
                np.nanstd(
                    index_array
                )
            )
        }

        return stats

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Vegetation statistics failed"
        )