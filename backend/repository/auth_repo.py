from fastapi import HTTPException, status
from models import User
from security import Hash
from datetime import timedelta


async def login(request, auth, db):
    user = db.query(User).filter(User.username == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    if not Hash.verify_password(
        plain_password=request.password, hashed_password=user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    expires = timedelta(hours=4)

    access_token = await auth.create_access_token(
        subject=user.id,
        fresh=True,
        expires_time=expires,
    )
    refresh_token = await auth.create_refresh_token(subject=user.id)

    return {"access": access_token, "refresh": refresh_token}


def refresh_token(token):
    pass
