import numpy as np

from app.core.logger import logger

def calculate_statistics(
    values
):
    try:
        logger.info(
            "Calculating statistics..."
        )

        stats = {
            "mean":
                float(
                    np.mean(values)
                ),

            "min":
                float(
                    np.min(values)
                ),

            "max":
                float(
                    np.max(values)
                ),

            "std":
                float(
                    np.std(values)
                )
        }

        return stats

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Statistics calculation failed"
        )