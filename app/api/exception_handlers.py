from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.models.domain.exceptions.interfaces import ConflictException, NotFoundException
from app.services.exceptions.interfaces import BadRequestException

async def not_found_handler(request: Request, exc: NotFoundException) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "resource not found",
            "message": str(exc),
            "id": exc.id
        }
    )

async def conflict_handler(request: Request, exc: ConflictException) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "resource already exists",
            "message": str(exc),
            "id": exc.id
        }
    )

async def bad_request_handler(request: Request, exc: BadRequestException) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "bad request",
            "message": str(exc),
        }
    )