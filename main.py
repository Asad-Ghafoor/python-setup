from middlewares.cors import add_cors_middleware
from middlewares.rate_limit import rate_limiter
from middlewares.error_handler import custom_exception_handler
from middlewares.logging import LoggingMiddleware
from app.route import router

from db.database import engine
from db.models import Base
from config.settings import settings
from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title=settings.project_name,
    description=settings.project_description,
    version=settings.project_version
)

Base.metadata.create_all(bind=engine)

add_cors_middleware(app)
app.add_middleware(
    LoggingMiddleware if settings.enable_logging else None  
)
app.add_exception_handler(Exception, custom_exception_handler)
app.middleware("http")(rate_limiter)

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=True)