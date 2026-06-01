from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from app.core.logger import logger

def evaluate_model(
    y_true,
    y_pred
):
    try:
        logger.info(
            "Evaluating model..."
        )

        metrics = {
            "accuracy":
                accuracy_score(
                    y_true,
                    y_pred
                ),

            "precision":
                precision_score(
                    y_true,
                    y_pred,
                    average="weighted"
                ),

            "recall":
                recall_score(
                    y_true,
                    y_pred,
                    average="weighted"
                ),

            "f1_score":
                f1_score(
                    y_true,
                    y_pred,
                    average="weighted"
                )
        }

        return metrics

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Model evaluation failed"
        )