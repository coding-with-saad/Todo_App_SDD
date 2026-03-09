from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth.middleware import AuthMiddleware
from .api.todos import router as todos_router
from .api.auth import router as auth_router
from .database.session import init_db
from .models.user import User
from .models.todo import Todo

app = FastAPI(title="Todo App API")

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Authentication Middleware
app.add_middleware(AuthMiddleware)

@app.on_event("startup")
def on_startup():
    # init_db()  # Commented out to prevent hanging; tables confirmed in Neon
    pass

# Include Routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(todos_router, prefix="/todos", tags=["Todos"])

@app.get("/")
async def root():
    return {"message": "Todo App API is running"}
