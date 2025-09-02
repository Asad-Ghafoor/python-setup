from fastapi import APIRouter
from app.routes.auth_routes import router as auth_router

router = APIRouter(prefix="/auth")



router.include_router(auth_router)  