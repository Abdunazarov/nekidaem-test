# thirdparty
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import func

# project
from db.models.post_model import Post
from db.models.subscription_model import Subscription


async def get_news_feed(session: AsyncSession, user_id: int, skip: int, limit: int):
    subquery = select(Subscription.blog_id).filter(Subscription.user_id == user_id).subquery()
    query = (
        select(Post)
        .join(subquery, Post.blog_id == subquery.c.blog_id)
        .order_by(Post.created_at.desc())
        .offset(skip)
        .limit(limit)
    )
    result = await session.execute(query)
    posts = result.scalars().all()
    return posts
