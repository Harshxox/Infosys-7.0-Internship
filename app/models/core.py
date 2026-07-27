from sqlalchemy import Column, String, Float, Integer, DateTime, Boolean, JSON, Enum
from app.database.connection import Base
import datetime
import uuid

class Customer(Base):
    __tablename__ = "customers"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=True) # Changed to True so registration works without a name
    email = Column(String, unique=True, index=True, nullable=False)
    
    # ADDED THIS COLUMN:
    hashed_password = Column(String, nullable=False) 
    
    billing_country = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Plan(Base):
    __tablename__ = "plans"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    billing_interval = Column(String, nullable=False) # e.g., 'monthly', 'annual'
    trial_period_days = Column(Integer, default=0)
    feature_entitlements = Column(JSON, nullable=True)
    status = Column(String, default="active") # 'active' or 'archived'
    created_at = Column(DateTime, default=datetime.datetime.utcnow)