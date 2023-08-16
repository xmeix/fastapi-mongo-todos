from pydantic import BaseModel, EmailStr,Field

class User(BaseModel):
    name: str = (Field(default=None),)
    email: EmailStr = (Field(default=None),)
    password: bool = (Field(default=None),)
    
    