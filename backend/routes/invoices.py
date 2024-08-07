from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
import uuid
from typing import List


from database import get_db
from models import Invoice
from schemas import CreateInvoice, UpdateInvoice, ShowInvoice
from . import create_route

router = create_route(
    prefix="invoices",
    tags="Invoices",
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[ShowInvoice],
)
async def get_invoices(
    db: Session = Depends(get_db),
):
    invoices = db.query(Invoice).all()
    return invoices
