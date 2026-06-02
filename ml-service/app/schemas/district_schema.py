from pydantic import (
    BaseModel,
    Field
)

class DistrictRequest(
    BaseModel
):
    district_name: str = Field(
        ...,
        example="Nashik"
    )

    state: str = Field(
        ...,
        example="Maharashtra"
    )

    latitude: float = Field(
        ...,
        example=19.9975
    )

    longitude: float = Field(
        ...,
        example=73.7898
    )