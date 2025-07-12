from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.models.domain.exceptions import NotFoundException


async def not_found_handler(request: Request, exc: NotFoundException) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "resource not found",
            "message": str(exc),
            "id": exc.id
        }
    )