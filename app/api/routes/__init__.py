from fastapi import APIRouter

from app.api.routes.v1 import users_router, restaurants_router, restaurant_orders_router, menu_items_router

v1router = APIRouter(prefix="/v1")
v1router.include_router(users_router)
v1router.include_router(restaurants_router)
v1router.include_router(restaurant_orders_router)
v1router.include_router(menu_items_router)