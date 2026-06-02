from fastapi import APIRouter

import rasterio
import numpy as np
import os

router = APIRouter()

@router.post("/satellite/process")
def process_satellite(payload: dict):

    try:

        image_path = payload["image_path"]

        district_name = payload["district_name"]

        provider = payload["provider"]

        if not os.path.exists(image_path):

            return {
                "success": False,
                "message": "TIFF file not found"
            }

        with rasterio.open(image_path) as src:

            # Sentinel-2 Bands
            # B04 = Red
            # B08 = NIR

            red = src.read(3).astype(float)

            nir = src.read(4).astype(float)

            # NDVI Calculation
            ndvi = (
                (nir - red)
                /
                (nir + red + 1e-10)
            )

            ndvi_mean = float(
                np.mean(ndvi)
            )

        # Risk Analysis
        if ndvi_mean < 0.3:

            risk = "HIGH"

        elif ndvi_mean < 0.6:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        return {
            "success": True,

            "district":
                district_name,

            "provider":
                provider,

            "ndvi_mean":
                ndvi_mean,

            "risk_level":
                risk
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }