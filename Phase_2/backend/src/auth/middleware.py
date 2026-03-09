from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from .jwt import verify_jwt, get_user_id_from_payload

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Allow CORS preflight requests
        if request.method == "OPTIONS":
            return await call_next(request)

        # Allow open routes
        open_prefixes = ["/auth/", "/docs", "/openapi.json"]
        if any(request.url.path.startswith(prefix) for prefix in open_prefixes) or request.url.path == "/":
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Missing or invalid authentication header"}
            )

        token = auth_header.split(" ")[1]
        payload = verify_jwt(token)
        
        if not payload:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Could not validate credentials"}
            )

        user_id = get_user_id_from_payload(payload)
        if not user_id:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "User ID not found in token"}
            )

        # Attach user_id to request state for use in routers
        request.state.user_id = user_id
        
        response = await call_next(request)
        return response
