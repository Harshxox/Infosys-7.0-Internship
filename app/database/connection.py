import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Load the .env file
load_dotenv()

# 2. Fetch the URL
DATABASE_URL = os.getenv("DATABASE_URL")

# --- DEBUGGING BLOCK ---
print("\n" + "="*50)
print(f"DEBUG: Python thinks DATABASE_URL is -> {DATABASE_URL}")
print("="*50 + "\n")

# 3. Force a hardcoded fallback if .env fails
if not DATABASE_URL:
    print("WARNING: .env file failed to load! Using hardcoded URL instead...\n")
    DATABASE_URL = "postgresql://postgres:123456@localhost:5432/billflow"

# 4. Create the engine
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Add this to the bottom of app/database/connection.py

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()