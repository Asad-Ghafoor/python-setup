from fastapi import Request, HTTPException
from utils.response_formatter import format_response
from logger.logger import logger

async def custom_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error: {exc}")

    if isinstance(exc, HTTPException):
        return format_response(
            status=exc.status_code,
            message=exc.detail,
            data=None,
            notify=False,
            request=request
        )

    return format_response(
        status=500,
        message="Internal Server Error",
        data=None,
        notify=False,
        request=request
    )
