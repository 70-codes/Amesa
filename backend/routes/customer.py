from fastapi import status, HTTPException, Depends
import uuid
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime


from . import create_route
from database import get_db
from models import Customer
from schemas import CreateCustomer, ShowCustomer, UpdateCustomer


router = create_route(
    prefix="customers",
    tags="Customers",
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowCustomer,
)
async def create_customer(
    request: CreateCustomer,
    db: Session = Depends(get_db),
):
    request.id = str(uuid.uuid4())
    request.created_at = str(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    request.updated_at = str(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    new_customer = Customer(**request.model_dump())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


@router.get(
    "/",
    response_model=List[ShowCustomer],
    status_code=status.HTTP_200_OK,
)
async def get_all_customers(
    db: Session = Depends(get_db),
):
    customers = db.query(Customer).all()
    return customers


@router.get(
    "/{id}",
    response_model=ShowCustomer,
    status_code=status.HTTP_200_OK,
)
async def get_customer(
    id: str,
    db: Session = Depends(get_db),
):
    customer = db.query(Customer).filter(Customer.id == id).first()
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )
    return customer


@router.patch(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowCustomer,
)
async def update_customer(
    request: UpdateCustomer,
    id: str,
    db: Session = Depends(get_db),
):
    customer = db.query(Customer).filter(Customer.id == id).first()
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )
    if request.name is not None:
        customer.name = request.name
    if request.email is not None:
        customer.email = request.email
    if request.phone is not None:
        customer.phone = request.phone
    if request.address is not None:
        customer.address = request.address
    if request.updated_at is not None:
        customer.updated_at = str(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )

    db.commit()
    db.refresh(customer)
    return customer


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
)
async def delete_customer(
    id: str,
    db: Session = Depends(get_db),
):
    customer = db.query(Customer).filter(Customer.id == id).first()
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )
    db.delete(customer)
    db.commit()
    return {
        "detail": "Customer deleted successfully",
    }
