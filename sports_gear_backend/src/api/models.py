"""
Database models and ORM setup for the Sports Gear ecommerce backend.
Defines: User, ProductCategory, Product, Cart, CartItem, Order, OrderItem.

Uses SQLite and SQLAlchemy for ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean, Text, create_engine, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta
import os

# Base for ORM models
Base: DeclarativeMeta = declarative_base()

# --- Models ---

# PUBLIC_INTERFACE
class User(Base):
    """
    User for the ecommerce system.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(256), unique=True, nullable=False, index=True)
    hashed_password = Column(String(256), nullable=False)
    full_name = Column(String(128), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())

    carts = relationship("Cart", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")


# PUBLIC_INTERFACE
class ProductCategory(Base):
    """
    Product categories (e.g., Shoes, Apparel).
    """
    __tablename__ = "product_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False, unique=True)
    description = Column(Text, nullable=True)

    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")


# PUBLIC_INTERFACE
class Product(Base):
    """
    Products for sale.
    """
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False, index=True)
    description = Column(Text, nullable=True)
    image_url = Column(String(512))
    price = Column(Float, nullable=False)
    available_sizes = Column(String(256), nullable=True)  # e.g., "S,M,L,XL"
    category_id = Column(Integer, ForeignKey("product_categories.id"))

    category = relationship("ProductCategory", back_populates="products")
    cart_items = relationship("CartItem", back_populates="product", cascade="all, delete-orphan")
    order_items = relationship("OrderItem", back_populates="product", cascade="all, delete-orphan")


# PUBLIC_INTERFACE
class Cart(Base):
    """
    Shopping cart for a user.
    """
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    checked_out = Column(Boolean, default=False)

    user = relationship("User", back_populates="carts")
    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")


# PUBLIC_INTERFACE
class CartItem(Base):
    """
    Item in a user's cart.
    """
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    selected_size = Column(String(32), nullable=True)

    cart = relationship("Cart", back_populates="items")
    product = relationship("Product", back_populates="cart_items")


# PUBLIC_INTERFACE
class Order(Base):
    """
    Completed order.
    """
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    status = Column(String(32), default="pending")  # e.g., pending, paid, shipped, delivered, cancelled
    total_amount = Column(Float, nullable=False)

    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


# PUBLIC_INTERFACE
class OrderItem(Base):
    """
    Line item in an order.
    """
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_at_purchase = Column(Float, nullable=False)
    selected_size = Column(String(32), nullable=True)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")


# --- Database Engine/Session Management ---

DB_FILENAME = os.getenv("SQLITE_DB_FILENAME", "sports_gear.db")
DB_PATH = os.path.join(os.path.dirname(__file__), "../../../", DB_FILENAME)
DATABASE_URL = f"sqlite:///{os.path.abspath(DB_PATH)}"

# PUBLIC_INTERFACE
def get_engine(echo=False):
    """
    Returns a SQLAlchemy engine for the SQLite database.
    """
    return create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=echo)

# PUBLIC_INTERFACE
def get_session_local():
    """
    Returns a SQLAlchemy sessionmaker (local session factory) for dependency injection.
    """
    return sessionmaker(autocommit=False, autoflush=False, bind=get_engine())

# PUBLIC_INTERFACE
def init_db():
    """
    Initializes the SQLite DB and creates all tables if not present.
    """
    engine = get_engine()
    Base.metadata.create_all(bind=engine)

