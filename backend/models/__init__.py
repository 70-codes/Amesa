from sqlalchemy.orm import relationship
from sqlalchemy import (
    String,
    Integer,
    Column,
    Boolean,
    ForeignKey,
)
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    fname = Column(String)
    lname = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(String)
    updated_at = Column(String)


class Product(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    m_price = Column(Integer)
    s_price = Column(Integer)
    quantity = Column(Integer)
    category = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    user_id = Column(String, ForeignKey("users.id"))

    sales = relationship("Sale", back_populates="product")


class Sale(Base):
    __tablename__ = "sales"
    id = Column(String, primary_key=True, index=True)
    quantity = Column(Integer)
    total_price = Column(Integer)
    type = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    product_id = Column(String, ForeignKey("products.id"))
    user_id = Column(String, ForeignKey("users.id"))
    invoice_id = Column(String, ForeignKey("invoices.id"))

    invoice = relationship("Invoice", back_populates="sales")
    product = relationship("Product", back_populates="sales")


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(String, primary_key=True, index=True)
    number = Column(Integer)
    status = Column(String)
    total_price = Column(Integer)
    due_date = Column(String)
    customer_id = Column(String, ForeignKey("customers.id"))

    sales = relationship("Sale", back_populates="invoice")
    customer = relationship(
        "Customer", back_populates="invoices", foreign_keys=[customer_id]
    )


class Customer(Base):
    __tablename__ = "customers"
    id = Column(String, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    invoice_id = Column(String, ForeignKey("invoices.id"))

    invoices = relationship(
        "Invoice", back_populates="customer", foreign_keys="Invoice.customer_id"
    )
