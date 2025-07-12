from typing import Any

from fastapi import APIRouter, status

from app.models.schemas.user import UserCreate, UserResponse, UserUpdate
from app.api.dependencies import UserServiceDep

router: APIRouter = APIRouter(prefix="/users", tags=["Users"])

@router.get(
    path="/{id}",
    status_code=status.HTTP_200_OK,
    summary="Get a user",
    response_model=UserResponse
)
def get(
    user_id: int,
    user_service: UserServiceDep
) -> Any:
    return user_service.get(user_id)

@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    summary="Create a user",
    response_model=UserResponse
)
def create(
    user_create: UserCreate,
    user_service: UserServiceDep
) -> Any:
    ...


@router.patch(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    response_model=UserResponse
)
def update(
    user_update: UserUpdate,
    user_service: UserServiceDep
) -> Any:
    ...


@router.delete(
    path="/{id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
)
def delete(
    user_id: int,
    user_service: UserServiceDep
) -> None:
    ...

