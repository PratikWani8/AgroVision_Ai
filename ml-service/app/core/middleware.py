from fastapi import Request

from app.core.logger import logger

async def log_requests(
    request: Request,
    call_next
):
    logger.info(
        f"{request.method} {request.url}"
    )

    response = await call_next(
            request
        )

    return response