from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from . import create_route
from models import Sale
from schemas import ShowSale

router = create_route(
    prefix="sales",
    tags="Sales",
)


@router.get("/", response_model=List[ShowSale])
async def get_all(
    db: Session = Depends(get_db),
):
    sales = db.query(Sale).all()
    return sales


@router.get("/{id}", response_model=ShowSale)
async def get_sale(
    id: str,
    db: Session = Depends(get_db),
):
    sale = db.query(Sale).filter(Sale.id == id).first()
    if not sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale not found",
        )
    return sale
