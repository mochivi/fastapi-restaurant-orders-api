from fastapi import FastAPI

from app.api import api_router as api_router
from app.api.exception_handlers import not_found_handler
from app.core.config import settings

from app.core.exceptions import global_exception_handler
from app.models.domain.exceptions import UserNotFoundException

app: FastAPI = FastAPI(
    title=settings.TITLE,
)

# Register routes
app.include_router(api_router)

# Register exceptions
app.add_exception_handler(UserNotFoundException, not_found_handler) # type: ignore

# Global exception handler
app.add_exception_handler(Exception, global_exception_handler)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)