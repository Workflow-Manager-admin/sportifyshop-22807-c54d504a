"""
Seed categories and demo products for the sports gear backend database.

- Adds a handful of product categories (if not present).
- Adds demo products to each category.
- Idempotent: safe to call multiple times.
"""

from sqlalchemy.orm import Session
from .models import ProductCategory, Product

# PUBLIC_INTERFACE
def seed_categories_and_products(db: Session):
    """
    Seed demo categories and products for sports gear. Idempotent for initial setup.

    Args:
        db (Session): SQLAlchemy database session.

    Seeds:
        - Shoes, Shirts, Trousers, Watches
        - Example products in each category (if not already present)
    """
    # ---- Categories ---- #
    categories = [
        {"name": "Shoes", "description": "Running, training, sports shoes"},
        {"name": "Shirts", "description": "Sport and exercise shirts"},
        {"name": "Trousers", "description": "Sport pants, leggings, shorts"},
        {"name": "Watches", "description": "Sport watches, fitness trackers"},
    ]
    for cat in categories:
        existing = db.query(ProductCategory).filter_by(name=cat["name"]).first()
        if not existing:
            db.add(ProductCategory(name=cat["name"], description=cat["description"]))
    db.commit()

    # ---- Demo Products ---- #
    demo_products = [
        {
            "name": "Adidas Ultraboost",
            "description": "Lightweight training shoe.",
            "image_url": "/static/images/adidas_ultraboost.jpg",
            "price": 120.0,
            "available_sizes": "7,8,9,10,11",
            "category_name": "Shoes",
        },
        {
            "name": "Nike Pegasus",
            "description": "Standard running shoe.",
            "image_url": "/static/images/nike_pegasus.jpg",
            "price": 110.0,
            "available_sizes": "7,8,9,10,11",
            "category_name": "Shoes",
        },
        {
            "name": "Under Armour Assert",
            "description": "Supportive and cushioned.",
            "image_url": "/static/images/ua_assert.jpg",
            "price": 90.0,
            "available_sizes": "8,9,10,11,12",
            "category_name": "Shoes",
        },
        {
            "name": "Reebok Nano",
            "description": "Versatile cross-trainer.",
            "image_url": "/static/images/reebok_nano.jpg",
            "price": 100.0,
            "available_sizes": "7,8,9,10",
            "category_name": "Shoes",
        },
        {
            "name": "Brooks Ghost",
            "description": "Soft and balanced running.",
            "image_url": "/static/images/brooks_ghost.jpg",
            "price": 130.0,
            "available_sizes": "9,10,11",
            "category_name": "Shoes",
        },
        {
            "name": "Saucony Ride 14",
            "description": "Cushioned everyday running.",
            "image_url": "/static/images/saucony_ride14.jpg",
            "price": 125.0,
            "available_sizes": "7,8.5,9.5,10.5",
            "category_name": "Shoes",
        },
        {
            "name": "NB Foam 1080",
            "description": "Premium comfort.",
            "image_url": "/static/images/nb_foam_1080.jpg",
            "price": 135.0,
            "available_sizes": "8,9,10",
            "category_name": "Shoes",
        },
        {
            "name": "Mizuno Wave Rider",
            "description": "Stable ride.",
            "image_url": "/static/images/mizuno_waverider.jpg",
            "price": 120.0,
            "available_sizes": "7,9,11",
            "category_name": "Shoes",
        },
        # Add Shirts
        {
            "name": "ASICS Kayano Tee",
            "description": "Breathable running shirt.",
            "image_url": "/static/images/asics_kayano.jpg",
            "price": 35.0,
            "available_sizes": "S,M,L,XL",
            "category_name": "Shirts",
        },
        {
            "name": "Puma Flyer Tee",
            "description": "Moisture-wicking workout shirt.",
            "image_url": "/static/images/puma_flyer.jpg",
            "price": 28.0,
            "available_sizes": "S,M,L",
            "category_name": "Shirts",
        }
    ]
    for prod in demo_products:
        category = db.query(ProductCategory).filter_by(name=prod["category_name"]).first()
        if not category:
            continue  # Defensive: skip if category missing
        exists = db.query(Product).filter_by(name=prod["name"], category_id=category.id).first()
        if not exists:
            db.add(Product(
                name=prod["name"],
                description=prod["description"],
                image_url=prod["image_url"],
                price=prod["price"],
                available_sizes=prod["available_sizes"],
                category_id=category.id
            ))
    db.commit()
