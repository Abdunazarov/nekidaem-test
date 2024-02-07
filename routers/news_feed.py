# stdlib
from typing import List

# thirdparty
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# project
from db.schemas.post_schemas import PostResponse
from db.db_setup import get_session
from services.news_feed_service import get_news_feed


router = APIRouter(prefix="/news_feed", tags=["NEWS FEED"])


@router.get("/user/{user_id}", response_model=List[PostResponse])
async def read_news_feed(user_id: int, skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    if limit > 500:
        raise HTTPException(status_code=400, detail="Cannot retrieve more than 500 posts at a time")
    posts = await get_news_feed(session, user_id, skip=skip, limit=limit)
    return posts


router = APIRouter(prefix="/news_feed", tags=["NEWS FEED"])
