from pydantic import (
    BaseModel,
    Field
)

class PredictionInput(
    BaseModel
):
    ndvi: float = Field(
        ...,
        example=0.72
    )

    ndwi: float = Field(
        ...,
        example=0.41
    )

    rainfall: float = Field(
        ...,
        example=120
    )

    humidity: float = Field(
        ...,
        example=78
    )

    temperature: float = Field(
        ...,
        example=32
    )

    soilMoisture: float = Field(
        ...,
        example=45
    )