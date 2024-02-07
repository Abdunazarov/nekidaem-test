# thirdparty
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import get_session

# project
from db.schemas.user_schemas import UserCreate, UserResponse
from services.user_service import create_user, delete_user

router = APIRouter(prefix="/users", tags=["USERS"])


@router.post("/", response_model=UserResponse)
async def create_user_endpoint(user: UserCreate, session: AsyncSession = Depends(get_session)):
    new_user = await create_user(session=session, user=user)
    if not new_user:
        raise HTTPException(status_code=400, detail="Failed to create user")
    return {"user": new_user}


@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user_endpoint(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await delete_user(session=session, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}
