from pydantic import (
    BaseModel
)

class TrainingRequest(
    BaseModel
):
    dataset_path: str

    model_name: str = "xgboost"