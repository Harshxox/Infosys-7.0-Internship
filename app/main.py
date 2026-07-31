from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import database engine and Base declarative mapping
# Adjust this path based on your actual project structure if necessary
from app.database.connection import engine, Base

# Import models so SQLAlchemy knows they exist before creating tables
import app.models.core

# Import routers
# We are assuming Step 1 (creating app/api/users.py) was completed successfully
from app.routers import auth
from app.api import plans
from app.api import users  # <-- NEW: Imported the new users router

# Create all tables in the database (if they don't exist yet)
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI(
    title="BillWise API",
    description="Backend API for the Automated Billing Platform",
    version="1.0.0"
)

# Configure CORS (Cross-Origin Resource Sharing)
# This allows your Vanilla JS frontends (Admin and Customer) to communicate safely with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your frontend's actual URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all route handlers
app.include_router(auth.router)
app.include_router(plans.router)
app.include_router(users.router)  # <-- NEW: Plugged the users router into the app

# Root endpoint for basic API health check
@app.get("/")
def root():
    return {
        "status": "success", 
        "message": "BillWise API is running and database is connected!"
    }