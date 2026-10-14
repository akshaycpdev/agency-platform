from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from database import check_database_connection
from routers.auth import router as auth_router
from routers.users import router as users_router

app = FastAPI(
    title="Agency Platform API",
    description="Backend API for our software agency platform",
    version="0.1.0",
)

app.include_router(users_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Agency Platform API is running!",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "agency-platform-backend",
    }


@app.get("/health/database")
def database_health_check():
    try:
        database_name = check_database_connection()
        return {
            "status": "connected",
            "database": database_name,
        }
    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed",
        )
