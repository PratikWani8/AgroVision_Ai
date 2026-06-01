import os
import joblib
import numpy as np

from app.core.logger import logger

MODEL_PATH = "models/xgboost_model.pkl"

model = None

def load_model():

    global model

    try:

        if not os.path.exists(MODEL_PATH):

            logger.warning(
                "Model file not found. "
                "Train model first."
            )

            return None

        model = joblib.load(MODEL_PATH)

        logger.info(
            "Model loaded successfully"
        )

        return model

    except Exception as e:

        logger.error(str(e))

        return None

def predict_disease(payload):

    global model

    if model is None:
        model = load_model()

    if model is None:

        raise Exception(
            "Model not trained yet. "
            "Call /train first."
        )

    features = np.array([
        [
            payload.ndvi,
            payload.ndwi,
            payload.rainfall,
            payload.humidity,
            payload.temperature,
            payload.soilMoisture
        ]
    ])

    prediction = model.predict(features)[0]

    labels = {
        0: "LOW",
        1: "MEDIUM",
        2: "HIGH"
    }

    return {
        "risk_level":
            labels[int(prediction)],

        "prediction":
            int(prediction)
    }