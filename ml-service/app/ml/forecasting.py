import numpy as np

from app.core.logger import logger

def forecast_trend(
    time_series
):
    try:
        logger.info(
            "Forecasting trend..."
        )

        slope = np.polyfit(
                range(len(time_series)),
                time_series,
                1
            )[0]

        forecast = time_series[-1] + slope

        return {
            "forecast":
                float(forecast),

            "trend":
                float(slope)
        }

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Forecasting failed"
        )