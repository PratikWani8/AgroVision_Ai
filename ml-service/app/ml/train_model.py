import pandas as pd
import joblib
import os

from sklearn.model_selection import ( train_test_split )

from sklearn.metrics import ( accuracy_score )

from xgboost import XGBClassifier


def train_model():

    dataset_path = (
        "datasets/crop_disease_dataset.csv"
    )

    if not os.path.exists(dataset_path):

        raise Exception(
            f"Dataset not found: {dataset_path}"
        )

    df = pd.read_csv(dataset_path)

    X = df[
        [
            "ndvi",
            "ndwi",
            "rainfall",
            "humidity",
            "temperature",
            "soilMoisture"
        ]
    ]

    y = df["diseaseRisk"]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )
    )

    model = XGBClassifier()

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    os.makedirs(
        "models",
        exist_ok=True
    )

    joblib.dump(
        model,
        "models/xgboost_model.pkl"
    )

    return {
        "accuracy": float(accuracy)
    }