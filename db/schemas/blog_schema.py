# stdlib
from typing import List

# thirdparty
from pydantic import BaseModel, Field

# project
from db.schemas.post_schemas import PostResponse


class BlogCreate(BaseModel):
    title: str = Field(max_length=100, min_length=1)


class BlogResponse(BaseModel):
    id: int
    title: str
    posts: List[PostResponse] = []


class BlogUpdate(BaseModel):
    title: str = Field(max_length=100, min_length=1)
