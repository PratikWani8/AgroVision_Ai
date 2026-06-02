from fastapi import APIRouter

from app.ml.train_model import ( train_model )

import traceback

router = APIRouter()

@router.post("/train")
def train():

    try:

        result = train_model()

        return {
            "success": True,
            "metrics": result
        }

    except Exception as e:

        traceback.print_exc()

        return {
            "success": False,
            "message": str(e)
        }