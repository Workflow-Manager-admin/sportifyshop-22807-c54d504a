"""
CLI utility to ensure the categories (Shirts, Trousers, Shoes, Watches) exist in the database.

This will create or update the category entries without altering or deleting any products.
Usage:
  python ensure_categories.py
"""

from sqlalchemy.orm import sessionmaker
from src.api.models import get_engine, ProductCategory

def ensure_core_categories(session):
    categories_data = [
        {"name": "Shoes", "description": "Running, training, sports shoes"},
        {"name": "Shirts", "description": "Sport and exercise shirts"},
        {"name": "Trousers", "description": "Sport pants, leggings, shorts"},
        {"name": "Watches", "description": "Sport watches, fitness trackers"},
    ]
    for cat in categories_data:
        existing = session.query(ProductCategory).filter_by(name=cat["name"]).first()
        if existing:
            if cat["description"] and cat["description"].strip() != (existing.description or ""):
                existing.description = cat["description"]
                session.add(existing)
        else:
            session.add(ProductCategory(name=cat["name"], description=cat["description"]))
    session.commit()
    print("Ensured categories Shirts, Trousers, Shoes, Watches exist.")

if __name__ == "__main__":
    engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    ensure_core_categories(session)
    session.close()
