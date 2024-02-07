# thirdparty
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# project
from db.models.user_model import User
from db.schemas.user_schemas import UserCreate


async def create_user(session: AsyncSession, user: UserCreate):
    new_user = User(**user.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


async def delete_user(session: AsyncSession, user_id: int):
    query = delete(User).where(User.id == user_id).returning(User)
    result = await session.execute(query)
    await session.commit()
    return result.fetchone()
