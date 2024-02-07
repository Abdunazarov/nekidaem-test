# stdlib
from typing import List

# thirdparty
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import get_session

# project
from db.schemas.blog_schema import BlogCreate, BlogResponse, BlogUpdate
from services.blog_service import (
    create_user_blog,
    delete_blog,
    get_all_blogs,
    get_blog_by_id,
    update_blog,
)

router = APIRouter(prefix="/blogs", tags=["BLOGS"])


@router.post("/", response_model=BlogResponse)
async def create_blog_for_user(user_id: int, blog: BlogCreate, session: AsyncSession = Depends(get_session)):
    blog = await create_user_blog(session=session, user_id=user_id, blog=blog)

    if not blog:
        raise HTTPException(status_code=404, detail="User not found")

    return {"blog": blog}


@router.get("/{blog_id}", response_model=BlogResponse)
async def read_blog(blog_id: int, session: AsyncSession = Depends(get_session)):
    blog = await get_blog_by_id(session=session, blog_id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"blog": blog}


@router.put("/{blog_id}", response_model=BlogResponse)
async def update_blog(blog_id: int, blog: BlogUpdate, session: AsyncSession = Depends(get_session)):
    blog = await update_blog(session=session, blog_id=blog_id, blog=blog)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"blog": blog}


@router.delete("/{blog_id}", response_model=BlogResponse)
async def delete_blog(blog_id: int, session: AsyncSession = Depends(get_session)):
    blog = await delete_blog(session=session, blog_id=blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"blog": blog}


@router.get("/", response_model=List[BlogResponse])
async def read_all_blogs(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    blogs = await get_all_blogs(session=session, skip=skip, limit=limit)
    return {"blogs": blogs}
