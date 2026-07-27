from pydantic import BaseModel, EmailStr

# 1. Schema for data coming IN from the frontend (Registration)
class CustomerCreate(BaseModel):
    email: EmailStr
    password: str

# 2. Schema for data going OUT to the frontend
class CustomerResponse(BaseModel):
    id: str
    email: EmailStr

    # This tells Pydantic to read the data even if it is not a standard dictionary
    # (SQLAlchemy models return objects, not dictionaries)
    model_config = {"from_attributes": True}


from pydantic import BaseModel

class GoogleToken(BaseModel):
    token: str