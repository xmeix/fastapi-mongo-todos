from pydantic import BaseModel, Field

class Todo(BaseModel):
    name: str  = (Field(default=None),)
    description: str  = (Field(default=None),)
    complete: bool  = (Field(default=None),)
        