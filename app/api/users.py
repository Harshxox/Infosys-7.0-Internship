from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Import your database connection and models
from app.database.connection import get_db
import app.models.core as models

# Create the router
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    """
    Fetches all registered users from the database.
    Safely maps the fields so it won't crash if optional columns are missing.
    """
    # Assuming your SQLAlchemy model is named 'User' inside models.core
    users = db.query(models.Customer).all()
    
    result = []
    for u in users:
        # We use getattr() to safely pull data. 
        # If a column like 'is_active' doesn't exist in your DB, it defaults to True.
        result.append({
            "id": getattr(u, "id", None),
            "email": getattr(u, "email", "N/A"),
            # Fallback to email if username doesn't exist
            "username": getattr(u, "username", getattr(u, "email", "Unknown")), 
            "is_active": getattr(u, "is_active", True),
            "created_at": getattr(u, "created_at", None)
        })
        
    return result