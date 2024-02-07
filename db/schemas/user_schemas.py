# stdlib
from typing import List

# thirdparty
from pydantic import BaseModel, EmailStr, Field

# project
from db.schemas.post_schemas import PostResponse


class UserCreate(BaseModel):
    username: str = Field(max_length=36, min_length=4)
    email: EmailStr
    name: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    posts: List[PostResponse] = []
