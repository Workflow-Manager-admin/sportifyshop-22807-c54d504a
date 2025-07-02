from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from . import models

app = FastAPI(
    title="Sports Gear Ecommerce Backend",
    description="Backend for Sports Gear online shop. Handles users, products, carts, orders.",
    version="0.1.0",
    openapi_tags=[
        {"name": "health", "description": "Health and diagnostics"},
        {"name": "db", "description": "Database health"},
        {"name": "users", "description": "User management"},
        {"name": "catalog", "description": "Product catalog"},
        {"name": "cart", "description": "Shopping cart"},
        {"name": "orders", "description": "Order management"},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup event: Initialize DB
@app.on_event("startup")
def startup_event():
    """
    Initialize the database (create tables if not exist).
    """
    models.init_db()

@app.get("/", tags=["health"])
def health_check():
    """PUBLIC_INTERFACE: Simple app health check."""
    return {"message": "Healthy"}

# Dependency for getting a DB session
def get_db():
    """Yields a fresh SQLAlchemy DB session for each request."""
    SessionLocal = models.get_session_local()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# PUBLIC_INTERFACE
@app.get("/db/health", tags=["db"], summary="Database health check", response_model=dict)
def db_health_check(db: Session = Depends(get_db)):
    """
    Checks connectivity to the database.
    Returns: {"db_health": "ok"} if DB is connected and can be queried.
    Returns HTTP 503 if not available.
    """
    try:
        # Run a trivial query to test connectivity
        db.execute("SELECT 1")
        return {"db_health": "ok"}
    except Exception as exc:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"db_health": "unavailable", "detail": str(exc)},
        )
