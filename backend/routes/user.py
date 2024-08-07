from . import create_route
from fastapi import status, HTTPException, Depends
from sqlalchemy.orm import Session
import uuid
from datetime import datetime
from typing import List
from async_fastapi_jwt_auth import AuthJWT

from database import get_db
from schemas import CreateUser, ShowUser, UpdateUser
from models import User
from security import Hash
from repository import user_repo

router = create_route(
    prefix="user",
    tags="User",
)


@router.get(
    "/get-current-user",
    response_model=ShowUser,
    status_code=status.HTTP_200_OK,
)
async def get_current_user(
    db: Session = Depends(get_db),
    authorize: AuthJWT = Depends(),
) -> ShowUser:
    try:
        await authorize.jwt_required()
        current_user_id = await authorize.get_jwt_subject()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await user_repo.get_user_by_id(
        id=current_user_id,
        db=db,
    )


@router.post(
    "/create",
    response_model=ShowUser,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    request: CreateUser,
    db: Session = Depends(get_db),
):

    return await user_repo.create_user(
        request=request,
        db=db,
    )


@router.get(
    "/get-all",
    response_model=List[ShowUser],
    status_code=status.HTTP_200_OK,
)
async def get_all_users(db: Session = Depends(get_db)):
    return await user_repo.get_all_users(
        db=db,
    )


@router.get(
    "/{id}",
    response_model=ShowUser,
    status_code=status.HTTP_200_OK,
)
async def get_user(
    id: str,
    db: Session = Depends(get_db),
):
    return await user_repo.get_user_by_id(
        id=id,
        db=db,
    )


@router.patch(
    "/update/{id}",
    response_model=ShowUser,
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_user(
    id: str,
    request: UpdateUser,
    db: Session = Depends(get_db),
):
    return await user_repo.update_user(
        id=id,
        request=request,
        db=db,
    )


@router.delete(
    "/delete/{id}",
    status_code=status.HTTP_200_OK,
)
async def delete_user(
    id: str,
    db: Session = Depends(get_db),
):
    return await user_repo.delete_user(
        id=id,
        db=db,
    )
    pass
