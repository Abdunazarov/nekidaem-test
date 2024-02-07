# thirdparty
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete

# project
from db.models.subscription_model import Subscription
from db.schemas.subscription_schemas import SubscriptionCreate


async def create_subscription(session: AsyncSession, subscription: SubscriptionCreate):
    new_subscription = Subscription(**subscription.model_dump())
    session.add(new_subscription)
    await session.commit()
    await session.refresh(new_subscription)
    return new_subscription


async def delete_subscription(session: AsyncSession, subscription_id: int):
    query = delete(Subscription).where(Subscription.id == subscription_id).returning(Subscription)
    result = await session.execute(query)
    await session.commit()
    return result.fetchone()


async def get_user_subscriptions(session: AsyncSession, user_id: int):
    query = select(Subscription).filter(Subscription.user_id == user_id)
    result = await session.execute(query)
    subscriptions = result.scalars().all()
    return subscriptions


async def get_blog_subscribers(session: AsyncSession, blog_id: int):
    query = select(Subscription).filter(Subscription.blog_id == blog_id)
    result = await session.execute(query)
    subscribers = result.scalars().all()
    return subscribers
