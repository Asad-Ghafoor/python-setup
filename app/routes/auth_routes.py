from app.controller.auth_controller import login as login_controller, register as register_controller
from fastapi import APIRouter, Request
from validations.auth_validation import LoginRequest, RegisterRequest
router = APIRouter()

@router.post("/login")
def login(request: Request, login_request: LoginRequest):
    return login_controller(request, login_request)

@router.post("/register")
def register(request: Request, register_request: RegisterRequest):
    return register_controller(request, register_request)

