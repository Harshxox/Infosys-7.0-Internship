from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from passlib.context import CryptContext

# ==========================================
# 1. SECURITY CONFIGURATION
# ==========================================
# In a true production environment, SECRET_KEY should be moved to your .env file!
# For now, we will define it here to get the system running.
SECRET_KEY = "super_secret_billing_platform_key_change_me_later"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Tell passlib to use the bcrypt algorithm for hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ==========================================
# 2. PASSWORD HASHING & VERIFICATION
# ==========================================
def get_password_hash(password: str) -> str:
    """Takes a plain text password and returns a securely hashed version."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compares a typed password against the hashed version in the database."""
    return pwd_context.verify(plain_password, hashed_password)

# ==========================================
# 3. JWT TOKEN GENERATION
# ==========================================
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Generates a secure JSON Web Token for user sessions."""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})
    
    # Sign the token using our secret key and the HS256 algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt