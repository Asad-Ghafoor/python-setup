from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings

def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=settings.cors_allow_credentials,
        allow_methods=settings.cors_methods,
        allow_headers=settings.cors_headers,
    )