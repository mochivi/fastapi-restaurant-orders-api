import logging

from fastapi import Request, status
from fastapi.responses import JSONResponse
from pydantic.json_schema import JsonRef

logger = logging.getLogger(__name__)

async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.error(f"Unhandled exception: {exc}", exc_info=True)

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred"
        }
    )