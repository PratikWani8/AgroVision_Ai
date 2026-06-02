from pydantic import (
    BaseModel,
    Field
)

class SatelliteProcessingRequest(
    BaseModel
):
    image_path: str = Field(
        ...,
        example="./satellite_data/raw/sample.tif"
    )

    district_name: str = Field(
        ...,
        example="Pune"
    )

    provider: str = Field(
        default="sentinel",
        example="sentinel"
    )