# thirdparty
from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# project
from db.models.blog_model import Blog
from db.schemas.blog_schema import BlogCreate, BlogUpdate


async def get_blog_by_user_id(session: AsyncSession, user_id: int):
    query = select(Blog).filter(Blog.user_id == user_id)
    result = await session.execute(query)
    return result.scalar()


async def create_user_blog(session: AsyncSession, user_id: int, blog: BlogCreate):
    new_blog = Blog(user_id=user_id, **blog.dict())
    session.add(new_blog)
    await session.commit()
    await session.refresh(new_blog)
    return new_blog


async def get_blog_by_id(session: AsyncSession, blog_id: int):
    query = select(Blog).filter(Blog.id == blog_id)
    result = await session.execute(query)
    return result.scalar()


async def update_blog(session: AsyncSession, blog_id: int, blog: BlogUpdate):
    query = (
        update(Blog)
        .where(Blog.id == blog_id)
        .values(**blog.dict())
        .returning(Blog)
        .execution_options(synchronize_session="fetch")
    )
    result = await session.execute(query)
    await session.commit()
    return result.fetchone()


async def delete_blog(session: AsyncSession, blog_id: int):
    query = delete(Blog).where(Blog.id == blog_id)
    await session.execute(query)
    await session.commit()


async def get_all_blogs(session: AsyncSession, skip: int, limit: int):
    query = select(Blog).offset(skip).limit(limit)
    result = await session.execute(query)
    blogs = result.scalars().all()
    return blogs
