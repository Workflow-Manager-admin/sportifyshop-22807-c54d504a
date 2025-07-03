"""
Seed categories and sports gear products for the backend database.

- Removes all old products before seeding.
- Ensures categories exist.
- Adds 10 shirts, 10 trousers, 10 watches, and 10 shoes (with images/prices).
"""

from sqlalchemy.orm import Session
from sqlalchemy import text
from .models import ProductCategory, Product

# PUBLIC_INTERFACE
def seed_categories_and_products(db: Session):
    """
    PUBLIC_INTERFACE
    Remove all old products and seed 10 shirts, 10 trousers, 10 watches, and 10 shoes
    with images and prices. Ensures required product categories exist.
    """
    # ---- Categories - ensure present ---- #
    categories_data = [
        {"name": "Shoes", "description": "Running, training, sports shoes"},
        {"name": "Shirts", "description": "Sport and exercise shirts"},
        {"name": "Trousers", "description": "Sport pants, leggings, shorts"},
        {"name": "Watches", "description": "Sport watches, fitness trackers"},
    ]
    categories = {}
    for cat in categories_data:
        existing = db.query(ProductCategory).filter_by(name=cat["name"]).first()
        if not existing:
            existing = ProductCategory(name=cat["name"], description=cat["description"])
            db.add(existing)
            db.commit()
            db.refresh(existing)
        categories[cat["name"]] = existing

    # ---- Products: remove ALL old, then seed exactly 10 of each required type ---- #
    db.execute(text("DELETE FROM product;"))  # hard reset
    db.commit()

    demo_products = []
    # 10 Shoes
    for i in range(1, 11):
        demo_products.append({
            "name": f"Sport Shoe Model {i}",
            "description": f"High Performance Running Shoe Model {i}",
            "image_url": f"https://img.example.com/shoe{i}.jpg",
            "price": 70 + i * 3,  # Vary price a little
            "available_sizes": "7,8,9,10,11",
            "category_name": "Shoes"
        })
    # 10 Shirts
    for i in range(1, 11):
        demo_products.append({
            "name": f"Sports Shirt {i}",
            "description": f"Breathable Sports Shirt Style {i}",
            "image_url": f"https://img.example.com/shirt{i}.jpg",
            "price": 20 + i * 2.5,
            "available_sizes": "S,M,L,XL",
            "category_name": "Shirts",
        })
    # 10 Trousers
    for i in range(1, 11):
        demo_products.append({
            "name": f"Sport Trouser {i}",
            "description": f"Flexible sports trousers #{i} for all activities.",
            "image_url": f"https://img.example.com/trouser{i}.jpg",
            "price": 30 + i * 1.8,
            "available_sizes": "S,M,L,XL",
            "category_name": "Trousers"
        })
    # 10 Watches
    for i in range(1, 11):
        demo_products.append({
            "name": f"Sports Watch {i}",
            "description": f"Durable water resistant sports watch model {i}.",
            "image_url": f"https://img.example.com/watch{i}.jpg",
            "price": 50 + i * 9.5,
            "available_sizes": "One Size",
            "category_name": "Watches"
        })

    for prod in demo_products:
        category = categories[prod["category_name"]]
        db.add(Product(
            name=prod["name"],
            description=prod["description"],
            image_url=prod["image_url"],
            price=prod["price"],
            available_sizes=prod["available_sizes"],
            category_id=category.id
        ))
    db.commit()
    print("Removed old products and seeded 10 each: shoes, shirts, trousers, watches.")

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from .models import engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    seed_categories_and_products(db)
