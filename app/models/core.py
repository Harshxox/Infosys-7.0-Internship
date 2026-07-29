from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, JSON
from sqlalchemy.sql import func
import uuid

# Assuming you have your Base imported from your database connection file
from app.database.connection import Base

class Customer(Base):
    __tablename__ = "customers"
    
    # FIXED: Column type changed to String, default casts UUID to a string
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    # Admin flag (Defaults to False for all normal signups)
    is_admin = Column(Boolean, default=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Plan(Base):
    __tablename__ = "plans"
    
    # FIXED: Column type changed to String, default casts UUID to a string
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    currency = Column(String, default="USD")
    billing_interval = Column(String, default="monthly") # 'monthly' or 'annual'
    trial_period_days = Column(Integer, default=0)
    
    # JSON column is perfect for an array of feature strings
    feature_entitlements = Column(JSON, default=list) 
    
    # True = Active/Available, False = Archived/Hidden
    status = Column(Boolean, default=True) 
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())