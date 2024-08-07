from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = (
        "2a3beb29fcb98dfc1a92016470b4566dcc470073855672b0c2f44831d148aa37"
    )
