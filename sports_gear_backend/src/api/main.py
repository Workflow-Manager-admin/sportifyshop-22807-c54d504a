import os
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status, Body, Path, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
import stripe
from sqlalchemy import text

from . import models

# ====== JWT CONFIG =======
SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-change-this-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 1 week
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ====== STRIPE CONFIG =======
STRIPE_KEY = os.getenv("STRIPE_SECRET_KEY", "sk_test_dummystripeapikey")
stripe.api_key = STRIPE_KEY

### ========= FASTAPI APP INSTANCE ========= ###
app = FastAPI(
    title="Sports Gear Ecommerce Backend",
    description="Backend for Sports Gear online shop. Handles users, products, carts, orders.",
    version="0.2.0",
    openapi_tags=[
        {"name": "health", "description": "Health and diagnostics"},
        {"name": "db", "description": "Database health"},
        {"name": "users", "description": "User management"},
        {"name": "auth", "description": "User authentication"},
        {"name": "catalog", "description": "Product catalog"},
        {"name": "cart", "description": "Shopping cart"},
        {"name": "orders", "description": "Order management"},
        {"name": "profile", "description": "User profile"},
        {"name": "checkout", "description": "Order checkout and payment"},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

######### ========== DB DEPENDENCY ============== #########

@app.on_event("startup")
def startup_event():
    """Initialize the database (create tables if not exist), and seed products/categories."""
    try:
        models.init_db()
        # Seed demo/real categories and product data if not present
        from .seed_data import seed_categories_and_products
        db_session_gen = get_db()
        db = next(db_session_gen)
        try:
            seed_categories_and_products(db)
        finally:
            db.close()
    except Exception as exc:
        import traceback
        print("Startup DB initialization failed:", exc, traceback.format_exc())

# PUBLIC_INTERFACE
def get_db():
    """Yield a fresh SQLAlchemy DB session for each request."""
    if not hasattr(get_db, "SessionLocal"):
        get_db.SessionLocal = models.get_session_local()
    db = get_db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ========= UTILS ========= #
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired.")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    user = db.query(models.User).filter(models.User.id == payload.get("sub")).first()
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="User inactive or not found")
    return user

def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=401, detail="Inactive user")
    return current_user

# ============ Pydantic Schemas (DTOs) ============ #

class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    full_name: Optional[str] = None

class UserProfileOut(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str]
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserProfileUpdate(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = Field(None, min_length=6)

class ProductCategoryOut(BaseModel):
    id: int
    name: str
    description: Optional[str]

    class Config:
        orm_mode = True

class ProductOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    image_url: Optional[str]
    price: float
    available_sizes: Optional[str]
    category: Optional[ProductCategoryOut]

    class Config:
        orm_mode = True

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)
    selected_size: Optional[str]

class CartItemOut(BaseModel):
    id: int
    product: ProductOut
    quantity: int
    selected_size: Optional[str]

    class Config:
        orm_mode = True

class CartOut(BaseModel):
    id: int
    items: List[CartItemOut]
    created_at: datetime
    checked_out: bool

    class Config:
        orm_mode = True

class OrderItemOut(BaseModel):
    id: int
    product: ProductOut
    quantity: int
    price_at_purchase: float
    selected_size: Optional[str]

    class Config:
        orm_mode = True

class OrderOut(BaseModel):
    id: int
    created_at: datetime
    total_amount: float
    status: str
    order_items: List[OrderItemOut]

    class Config:
        orm_mode = True

class StripeSessionResponse(BaseModel):
    checkout_url: str

# ---------- Health/Root ---------- #
@app.get("/", tags=["health"])
def health_check():
    """PUBLIC_INTERFACE: Simple app health check."""
    return {"message": "Healthy"}

# PUBLIC_INTERFACE
@app.get(
    "/db/health",
    tags=["db"],
    summary="Database health check",
    response_model=dict,
    responses={
        200: {
            "description": "Successfully connected to the database.",
            "content": {
                "application/json": {"example": {"db_health": "ok"}}
            },
        },
        503: {
            "description": "Database is unavailable or cannot be reached.",
            "content": {
                "application/json": {
                    "example": {
                        "db_health": "unavailable",
                        "detail": "Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')",
                    }
                }
            },
        },
    },
)
def db_health_check(db: Session = Depends(get_db)):
    """
    PUBLIC_INTERFACE: Checks connectivity to the database.

    Returns:
        200: {"db_health": "ok"} if DB is connected and can be queried.
        503: {"db_health": "unavailable", "detail": "..."} if not available.
    """
    try:
        db.execute(text("SELECT 1"))
        return {"db_health": "ok"}
    except Exception as exc:
        # Use HTTPException to allow OpenAPI docs to show response model
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"db_health": "unavailable", "detail": str(exc)},
        )

# ------------------ AUTH & USER MANAGEMENT -------------------

# PUBLIC_INTERFACE
@app.post(
    "/auth/register",
    response_model=UserProfileOut,
    tags=["auth"],
    summary="User registration",
    responses={
        201: {
            "description": "Successful registration, user created",
            "model": UserProfileOut,
        },
        409: {
            "description": "Email address is already registered. Registration cannot proceed.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Email already registered"
                    }
                }
            },
        },
        400: {
            "description": "General registration error (e.g., db error, failed creation)",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Could not create user"
                    }
                }
            },
        }
    },
)
def register_user(data: UserRegisterRequest, db: Session = Depends(get_db)):
    """
    Registers a new user by email, password, and full name.

    - Returns: user profile object on success (201).
    - Raises:
        - 409: If the email address is already registered and cannot be used.
        - 400: If the user could not be created for other reasons.

    Request body:
        - email: Email address of the user (must be unique)
        - password: User's password (min 6 characters)
        - full_name: Optional full name for the user

    Response:
        - On success: UserProfileOut (user details)
        - On duplicate email: {"detail": "Email already registered"} (409)
        - On other error: {"detail": "..."} (400)
    """
    if db.query(models.User).filter(models.User.email == data.email).first():
        raise HTTPException(status_code=409, detail="Email already registered")
    user = models.User(
        email=data.email,
        hashed_password=get_password_hash(data.password),
        full_name=data.full_name or "",
    )
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Could not create user")
    return user

# PUBLIC_INTERFACE
@app.post("/auth/login", response_model=UserLoginResponse, tags=["auth"], summary="User login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    OAuth2-compatible login endpoint.
    Accepts: username (email), password as form fields.
    Returns: access_token and token_type='bearer'.
    """
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    token = create_access_token({"sub": user.id})
    return UserLoginResponse(access_token=token)

# PUBLIC_INTERFACE
@app.get("/users/me", response_model=UserProfileOut, tags=["users", "profile"], summary="View logged-in user's profile")
def get_my_profile(current_user: models.User = Depends(get_current_active_user)):
    return current_user

# PUBLIC_INTERFACE
@app.put("/users/me", response_model=UserProfileOut, tags=["users", "profile"], summary="Update logged-in user's profile")
def update_my_profile(update: UserProfileUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if update.full_name is not None:
        current_user.full_name = update.full_name
    if update.password:
        current_user.hashed_password = get_password_hash(update.password)
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user

# ---------------- PRODUCT CATALOG (LIST, SEARCH, DETAIL) ------------

# PUBLIC_INTERFACE
@app.get("/categories", response_model=List[ProductCategoryOut], tags=["catalog"], summary="List all product categories")
def list_categories(db: Session = Depends(get_db)):
    return db.query(models.ProductCategory).all()

# PUBLIC_INTERFACE
@app.get("/products", response_model=List[ProductOut], tags=["catalog"], summary="List/search products")
def list_products(
    db: Session = Depends(get_db),
    q: Optional[str] = Query(None, description="Search by keyword"),
    category_id: Optional[int] = Query(None, description="Filter by category"),
    size: Optional[str] = Query(None, description="Filter by size (comma separated for multi-size)")
):
    query = db.query(models.Product)
    if q:
        query = query.filter(models.Product.name.ilike(f"%{q}%"))
    if category_id:
        query = query.filter(models.Product.category_id == category_id)
    if size:
        query = query.filter(models.Product.available_sizes.contains(size))
    return query.all()

# PUBLIC_INTERFACE
@app.get("/products/{product_id}", response_model=ProductOut, tags=["catalog"], summary="Get product details")
def get_product(product_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# ---------------- SHOPPING CART ---------------

# PUBLIC_INTERFACE
@app.get("/cart", response_model=CartOut, tags=["cart"], summary="Get my shopping cart")
def get_cart(current_user: models.User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    cart = (
        db.query(models.Cart)
        .filter(models.Cart.user_id == current_user.id, models.Cart.checked_out.is_(False))
        .first()
    )
    if not cart:
        cart = models.Cart(user_id=current_user.id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    db.refresh(cart)
    return cart

# PUBLIC_INTERFACE
@app.post("/cart/items", response_model=CartOut, tags=["cart"], summary="Add item to cart")
def add_item_to_cart(item: CartItemCreate, current_user: models.User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    cart = (
        db.query(models.Cart)
        .filter(models.Cart.user_id == current_user.id, models.Cart.checked_out.is_(False))
        .first()
    )
    if not cart:
        cart = models.Cart(user_id=current_user.id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    # Check if same product + size already in cart
    cart_item = (
        db.query(models.CartItem)
        .filter(
            models.CartItem.cart_id == cart.id,
            models.CartItem.product_id == item.product_id,
            models.CartItem.selected_size == item.selected_size,
        )
        .first()
    )
    if cart_item:
        cart_item.quantity += item.quantity
    else:
        cart_item = models.CartItem(
            cart_id=cart.id,
            product_id=item.product_id,
            quantity=item.quantity,
            selected_size=item.selected_size,
        )
        db.add(cart_item)
    db.commit()
    db.refresh(cart)
    return cart

# PUBLIC_INTERFACE
@app.put("/cart/items/{cart_item_id}", response_model=CartOut, tags=["cart"], summary="Update cart item quantity/size")
def update_cart_item(
    cart_item_id: int = Path(..., gt=0),
    item: CartItemCreate = Body(...),
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    cart_item = db.query(models.CartItem).join(models.Cart).filter(
        models.CartItem.id == cart_item_id,
        models.Cart.user_id == current_user.id,
        models.Cart.checked_out.is_(False)
    ).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    cart_item.quantity = item.quantity
    cart_item.selected_size = item.selected_size
    db.commit()
    db.refresh(cart_item.cart)
    return cart_item.cart

# PUBLIC_INTERFACE
@app.delete("/cart/items/{cart_item_id}", response_model=CartOut, tags=["cart"], summary="Remove cart item")
def remove_cart_item(
    cart_item_id: int = Path(..., gt=0),
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    cart_item = db.query(models.CartItem).join(models.Cart).filter(
        models.CartItem.id == cart_item_id,
        models.Cart.user_id == current_user.id,
        models.Cart.checked_out.is_(False)
    ).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    cart = cart_item.cart
    db.delete(cart_item)
    db.commit()
    db.refresh(cart)
    return cart

# ----------------- CHECKOUT & PAYMENT (STRIPE) ---------------

def calc_cart_total(cart: models.Cart, db: Session):
    total = 0.0
    for item in cart.items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if not product:
            continue
        total += product.price * item.quantity
    return round(total, 2)

# PUBLIC_INTERFACE
@app.post("/checkout/stripe-session", response_model=StripeSessionResponse, tags=["checkout"], summary="Create Stripe Checkout session")
def create_stripe_session(
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    cart = db.query(models.Cart).filter(models.Cart.user_id == current_user.id, models.Cart.checked_out.is_(False)).first()
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="No items in cart")
    # Build Stripe line items
    line_items = []
    for item in cart.items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if not product:
            continue
        line_items.append({
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": product.name,
                    "images": [product.image_url] if product.image_url else [],
                    "description": product.description or ""
                },
                "unit_amount": int(product.price * 100),
            },
            "quantity": item.quantity,
        })
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url=os.getenv("CHECKOUT_SUCCESS_URL", "https://example.com/success"),
            cancel_url=os.getenv("CHECKOUT_CANCEL_URL", "https://example.com/cancel"),
            metadata={"cart_id": cart.id, "user_id": current_user.id}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Stripe error: {str(e)}")
    return StripeSessionResponse(checkout_url=session.url)

# PUBLIC_INTERFACE
@app.post("/checkout/complete", response_model=OrderOut, tags=["checkout"], summary="Complete checkout and create order (simulate payment)")
def complete_checkout(
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    cart = db.query(models.Cart).filter(models.Cart.user_id == current_user.id, models.Cart.checked_out.is_(False)).first()
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="No items in cart")
    total = calc_cart_total(cart, db)
    # Simulate successful payment (Stripe webhook should do this in prod)
    order = models.Order(
        user_id=current_user.id,
        total_amount=total,
        status="paid"
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    # Create order items
    for item in cart.items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        order_item = models.OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=item.quantity,
            price_at_purchase=product.price,
            selected_size=item.selected_size,
        )
        db.add(order_item)
    # Mark cart as checked out
    cart.checked_out = True
    db.commit()
    db.refresh(order)
    return order

# --------------- ORDER HISTORY/USER ORDERS ---------------

# PUBLIC_INTERFACE
@app.get("/orders", response_model=List[OrderOut], tags=["orders"], summary="Get my order history")
def get_my_orders(current_user: models.User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    orders = db.query(models.Order).filter(models.Order.user_id == current_user.id).order_by(models.Order.created_at.desc()).all()
    return orders

# PUBLIC_INTERFACE
@app.get("/orders/{order_id}", response_model=OrderOut, tags=["orders"], summary="Get a specific order")
def get_order(order_id: int = Path(..., gt=0), current_user: models.User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.user_id == current_user.id, models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# ------- ADMIN and DEMO (OPTIONAL: For quick population/init) ---------
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = ""
    image_url: Optional[str] = None
    price: float
    available_sizes: Optional[str] = "M,L,XL"
    category_id: int = Field(..., gt=0)

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = ""

@app.post("/admin/category", response_model=ProductCategoryOut, tags=["catalog"], include_in_schema=False)
def admin_add_category(cat: CategoryCreate, db: Session = Depends(get_db)):
    category = models.ProductCategory(name=cat.name, description=cat.description)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

@app.post("/admin/product", response_model=ProductOut, tags=["catalog"], include_in_schema=False)
def admin_add_product(product: ProductCreate, db: Session = Depends(get_db)):
    prod = models.Product(**product.dict())
    db.add(prod)
    db.commit()
    db.refresh(prod)
    return prod

# ---- Improved Error handling middleware
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    import traceback
    from fastapi.responses import JSONResponse
    display_trace = bool(os.getenv("DEBUG", False)) or os.getenv("ENV", "development") == "development"
    trace = traceback.format_exc() if display_trace else "trace hidden"
    status_code = getattr(exc, "status_code", 500)
    detail = getattr(exc, "detail", str(exc))
    # Log the error server-side too
    print(f"Generic exception handler: {detail}\n{trace}")
    return JSONResponse(
        status_code=status_code,
        content={"detail": detail, "trace": trace},
    )
