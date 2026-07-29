from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import database engine and Base declarative mapping
from app.database.connection import engine, Base

# Import models so SQLAlchemy knows they exist before creating tables
import app.models.core


# Import routers
from app.routers import auth
from app.api import plans  # <-- NEW: Imported the plans router

# Create all tables in the database (if they don't exist yet)
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI(
    title="Subscription Management & Billing API",
    description="Backend API for the Automated Billing Platform",
    version="1.0.0"
)

# Configure CORS (Cross-Origin Resource Sharing)
# This allows your Vanilla JS frontend to communicate safely with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your frontend's actual URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all route handlers
app.include_router(auth.router)
app.include_router(plans.router)  # <-- NEW: Plugged the plans router into the app

# Root endpoint for basic API health check
@app.get("/")
def root():
    return {
        "status": "success", 
        "message": "Billing Platform API is running and database is connected!"
    }