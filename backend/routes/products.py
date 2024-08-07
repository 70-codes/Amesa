from fastapi import HTTPException, status, Depends, BackgroundTasks
from sqlalchemy.orm import Session
import uuid
from datetime import datetime
from typing import List
from async_fastapi_jwt_auth import AuthJWT


from database import get_db
from models import Product, Sale
from schemas import CreateProduct, UpdateProduct, ShowProduct, SellProduct


from . import create_route


router = create_route(
    prefix="product",
    tags="Products",
)


@router.post(
    "/",
    response_model=ShowProduct,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    request: CreateProduct,
    authorize: AuthJWT = Depends(),
    db: Session = Depends(get_db),
):
    # try:
    #     await authorize.jwt_required()
    # except Exception as e:
    #     raise HTTPException(status_code=401, detail="Unauthorized")
    request.id = str(uuid.uuid4())
    request.created_at = str(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    request.updated_at = str(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    new_product = Product(**request.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get(
    "/all",
    response_model=List[ShowProduct],
    status_code=status.HTTP_200_OK,
)
async def get_products(
    authorize: AuthJWT = Depends(),
    db: Session = Depends(get_db),
):
    try:
        await authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized")
    products = db.query(Product).all()
    return products


@router.get(
    "/{id}",
    response_model=ShowProduct,
    status_code=status.HTTP_200_OK,
)
async def get_product(
    id: str,
    authorize: AuthJWT = Depends(),
    db: Session = Depends(get_db),
):
    try:
        await authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized")

    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )
    return product
    pass


@router.patch(
    "/{id}",
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_product(
    request: UpdateProduct,
    product_id: str,
    authorize: AuthJWT = Depends(),
    db: Session = Depends(get_db),
):
    try:
        await authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized")
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )
    # Update product fields with new data
    if request.name is not None:
        product.name = request.name
    if request.m_price is not None:
        product.m_price = request.m_price
    if request.s_price is not None:
        product.s_price = request.s_price
    if request.quantity is not None:
        product.quantity = request.quantity
    if request.category is not None:
        product.category = request.category
    if request.user_id is not None:
        product.user_id = request.user_id

    product.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    db.commit()
    db.refresh(product)

    return {"message": "Product updated successfully", "product": product}


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
)
async def delete_product(
    id: str,
    authorize: AuthJWT = Depends(),
    db: Session = Depends(get_db),
):
    try:
        await authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized")
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )
    db.delete(product)
    db.commit()
    return {
        "detail": "Product deleted successfully",
    }


async def create_sale(product, sale_quantity, sale_type, db):
    if sale_quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Sale quantity must be greater than 0",
        )
    new_sale = Sale(
        id=str(uuid.uuid4()),
        product_id=product.id,
        quantity=sale_quantity,
        total_price=sale_quantity * product.s_price,
        type=sale_type,
        user_id=product.user_id,
        invoice_id=None,
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)


@router.post(
    "/{id}/sell",
    status_code=status.HTTP_201_CREATED,
)
async def sell_product(
    id: str,
    request: SellProduct,
    background_tasks: BackgroundTasks,
    authorize: AuthJWT = Depends(),
    db: Session = Depends(get_db),
):
    try:
        await authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized")
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )
    if request.quantity < 1:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be provided to sell product",
        )
    if product.quantity < 0:
        raise HTTPException(
            status_code=400,
            detail="Product out of stock",
        )
    else:
        product.quantity -= request.quantity
        product.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.commit()
        db.refresh(product)
        background_tasks.add_task(
            create_sale,
            product=product,
            sale_quantity=request.quantity,
            sale_type=request.sale_type,
            db=db,
        )
        return {
            "message": "Product sold successfully",
            "product": product,
        }
    pass
