from pydantic import (
    BaseModel,
    Field
)

class AnalyticsRequest(
    BaseModel
):
    ndvi: float = Field(
        ...,
        example=0.63
    )

    ndwi: float = Field(
        ...,
        example=0.39
    )

    temperature: float = Field(
        ...,
        example=31
    )

    humidity: float = Field(
        ...,
        example=76
    )