from sklearn.ensemble import ( IsolationForest )

from app.core.logger import logger

def detect_anomalies(
    dataframe
):
    try:
        logger.info(
            "Running anomaly detection..."
        )

        model = IsolationForest()

        predictions = model.fit_predict(
                dataframe
            )

        return predictions.tolist()

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Anomaly detection failed"
        )