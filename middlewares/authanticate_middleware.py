from fastapi import Request
from utils.response_formatter import format_response
from starlette.middleware.base import BaseHTTPMiddleware
from utils.helpers import verify_token
from config.settings import settings
from config.constants import missing_auth_token, invalid_auth_token

class AuthanticateMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in settings.skip_auth:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return format_response(status=401, message=missing_auth_token)

        token = auth_header.split(" ")[1]
        payload = verify_token(token)

        if not payload:
                return format_response(status=401, message=invalid_auth_token)

        request.state.user = payload
        return await call_next(request)
