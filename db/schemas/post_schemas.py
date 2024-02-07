# stdlib
from datetime import datetime

# thirdparty
from pydantic import BaseModel, Field


class PostCreate(BaseModel):
    title: str = Field(max_length=100, min_length=1)
    content: str = Field(gmax_length=140, min_length=1)


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
