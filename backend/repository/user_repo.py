import uuid
from datetime import datetime
from fastapi import HTTPException
from security import Hash

from models import User


async def get_user_by_username(username, db):
    return db.query(User).filter(User.username == username).first()


async def get_user_by_email(email, db):
    return db.query(User).filter(User.email == email).first()


async def get_user_by_id(id, db):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )
    return user


async def create_user(request, db):
    if await get_user_by_username(request.username, db):
        raise HTTPException(status_code=409, detail="Username already exists")
    if await get_user_by_email(request.email, db):
        raise HTTPException(status_code=409, detail="Email already exists")
    request.id = str(uuid.uuid4())
    request.password = Hash.get_password_hash(request.password)
    request.created_at = str(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    request.updated_at = str(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    user = User(**request.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def get_all_users(db):
    users = db.query(User).all()
    return users


async def update_user(id, request, db):
    user = await get_user_by_id(id, db)
    user.username = request.username if request.username else user.username
    user.email = request.email if request.email else user.email
    user.fname = request.fname if request.fname else user.fname
    user.lname = request.lname if request.lname else user.lname
    user.updated_at = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    db.commit()
    db.refresh(user)
    return user


async def delete_user(id, db):
    user = await get_user_by_id(id=id, db=db)
    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}
