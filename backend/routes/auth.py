from . import create_route
from database import get_db
from fastapi import Depends
from async_fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from pydantic import BaseModel
from schemas import UserLogin, Token
from repository import auth_repo

router = create_route(
    prefix="auth",
    tags="Auth",
)


@router.post("/login", response_model=Token)
async def login(
    request: UserLogin,
    auth: AuthJWT = Depends(),
    db: Session = Depends(get_db),
):
    return await auth_repo.login(
        request=request,
        auth=auth,
        db=db,
    )


@router.post(
    "/refresh-token",
    response_model=Token,
)
async def refresh_token():
    pass
