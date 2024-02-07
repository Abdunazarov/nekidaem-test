# stdlib
from typing import List

# thirdparty
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.schemas.subscription_schemas import SubscriptionCreate, SubscriptionResponse
from db.db_setup import get_session
from services.subscription_service import create_subscription, delete_subscription, get_user_subscriptions, get_blog_subscribers

router = APIRouter(prefix="/subscriptions", tags=["SUBSCRIPTIONS"])


@router.post("/", response_model=SubscriptionResponse)
async def subscribe(subscription: SubscriptionCreate, session: AsyncSession = Depends(get_session)):
    new_subscription = await create_subscription(session, subscription)
    if not new_subscription:
        raise HTTPException(status_code=400, detail="Failed to create subscription")
    return new_subscription


@router.delete("/{subscription_id}", response_model=SubscriptionResponse)
async def unsubscribe(subscription_id: int, session: AsyncSession = Depends(get_session)):
    subscription = await delete_subscription(session, subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription


@router.get("/user/{user_id}", response_model=List[SubscriptionResponse])
async def read_subscriptions_for_user(user_id: int, session: AsyncSession = Depends(get_session)):
    subscriptions = await get_user_subscriptions(session, user_id)
    return subscriptions


@router.get("/blog/{blog_id}", response_model=List[SubscriptionResponse])
async def read_subscribers_for_blog(blog_id: int, session: AsyncSession = Depends(get_session)):
    subscribers = await get_blog_subscribers(session, blog_id)
    return subscribers
