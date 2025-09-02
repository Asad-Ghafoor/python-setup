from fastapi.responses import JSONResponse
from fastapi import Request

def format_response(status: int, message: str, data=None, notify=False, request: Request = None):
    path = request.url.path if request else None
    return JSONResponse(
        status_code=status,
        content={
            "status": status,
            "message": message,
            "data": data,
            "notify": notify,
            "path": path
        }
    )
