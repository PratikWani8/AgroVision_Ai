from sklearn.ensemble import ( RandomForestClassifier )

from xgboost import ( XGBClassifier )

from app.core.logger import logger

def build_ensemble():
    try:
        logger.info(
            "Building ensemble model..."
        )

        models = {
            "random_forest":
                RandomForestClassifier(),

            "xgboost":
                XGBClassifier()
        }

        return models

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Ensemble model failed"
        )