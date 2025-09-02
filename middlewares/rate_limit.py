from fastapi import Request
from utils.response_formatter import format_response
from config.settings import settings
import time

requests_per_ip = {}

async def rate_limiter(request: Request, call_next):
    ip = request.client.host
    now = time.time()

    if ip not in requests_per_ip:
        requests_per_ip[ip] = []
    requests_per_ip[ip] = [t for t in requests_per_ip[ip] if now - t < 60]

    if len(requests_per_ip[ip]) >= settings.rate_limit_per_minute:
        return format_response(
            status=429,
            message="Too many requests",
            data=None,
            notify=False,
            request=request
        )

    requests_per_ip[ip].append(now)
    return await call_next(request)
