from validations.auth_validation import LoginRequest, RegisterRequest
from fastapi import Request
from utils.response_formatter import format_response
from app.services.auth_service import login as login_service, register as register_service

async def login(request: Request, login_request: LoginRequest):
    return format_response(status=200, message="Login route", data=login_service(login_request))

async def register(request: Request, register_request: RegisterRequest):
    return format_response(status=200, message="Register route", data=register_service(register_request))