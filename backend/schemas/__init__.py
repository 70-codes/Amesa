from pydantic import BaseModel
from typing import List


# +++++++++++++++++++++++++++++++++++++++++
# AUTH SCHEMAS
# +++++++++++++++++++++++++++++++++++++++++
class Token(BaseModel):
    access: str
    refresh: str


class UserLogin(BaseModel):
    username: str
    password: str


# +++++++++++++++++++++++++++++++++++++++++
# USER SCHEMAS
# +++++++++++++++++++++++++++++++++++++++++


class BaseUser(BaseModel):
    username: str
    email: str
    fname: str
    lname: str
    is_active: bool
    is_superuser: bool


class CreateUser(BaseUser):
    id: str
    password: str
    created_at: str
    updated_at: str


class UpdateUser(BaseUser):
    id: str
    updated_at: str


class ShowUser(BaseUser):
    id: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True


# +++++++++++++++++++++++++++++++++++++++++
# SALES SCHEMAS
# +++++++++++++++++++++++++++++++++++++++++
class BaseSale(BaseModel):
    id: str
    quantity: int
    total_price: int
    type: str
    product_id: str
    user_id: str


class CreateSale(BaseSale):
    created_at: str
    updated_at: str
    pass


class UpdateSale(BaseSale):
    updated_at: str


class ShowSale(BaseSale):
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True


# +++++++++++++++++++++++++++++++++++++++++
# PRODUCT SCHEMAS
# +++++++++++++++++++++++++++++++++++++++++


# Metadata classes
class ShowSaleInProduct(BaseSale):
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True


# Normal classes


class BaseProduct(BaseModel):
    id: str
    name: str
    m_price: int
    s_price: int
    quantity: int
    category: str
    user_id: str


class CreateProduct(BaseProduct):
    created_at: str
    updated_at: str


class UpdateProduct(BaseProduct):
    updated_at: str

    class Config:
        from_attributes = True


class ShowProduct(BaseProduct):
    created_at: str
    updated_at: str
    sales: List[ShowSaleInProduct]

    class Config:
        from_attributes = True


class SellProduct(BaseModel):
    sale_type: str
    quantity: int


# +++++++++++++++++++++++++++++++++++++++++
# CUSTOMER SCHEMA
# +++++++++++++++++++++++++++++++++++++++++


class BaseCustomer(BaseModel):
    id: str
    fname: str
    lname: str
    email: str
    phone: str
    address: str


class CreateCustomer(BaseCustomer):
    created_at: str
    updated_at: str


class UpdateCustomer(BaseCustomer):
    updated_at: str


class ShowCustomer(BaseCustomer):
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True


# +++++++++++++++++++++++++++++++++++++++++
# INVOICE SCHEMA
# +++++++++++++++++++++++++++++++++++++++++


class ShowCustomerInInvoice(BaseCustomer):

    class Config:
        from_attributes = True


class BaseInvoice(BaseModel):
    id: str
    number: int
    status: str
    total_price: int
    due_date: str
    customer_id: str


class CreateInvoice(BaseInvoice):
    created_at: str
    updated_at: str


class UpdateInvoice(BaseInvoice):
    updated_at: str


class ShowInvoice(BaseInvoice):
    customer: ShowCustomerInInvoice
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True
