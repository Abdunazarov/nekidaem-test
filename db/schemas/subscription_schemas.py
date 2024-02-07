# thirdparty
from pydantic import BaseModel, Field


class SubscriptionCreate(BaseModel):
    user_id: int
    blog_id: int


class SubscriptionResponse(BaseModel):
    id: int
    user_id: int
    blog_id: int
