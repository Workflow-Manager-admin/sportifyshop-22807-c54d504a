"""
Seed data for sports gear backend: Only seed 4 categories - Shirt, Trouser, Watches, and Shoes,
with 10 products each. Before seeding, REMOVES all other categories and products.
"""

from sqlalchemy.orm import Session
from . import models

# Categories to keep/seed
CATEGORIES_TO_KEEP = ["Shirt", "Trouser", "Watches", "Shoes"]

PRODUCT_IMAGES = {
    "Shirt": [
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab",
        "https://images.unsplash.com/photo-1484517186945-85072947a5d7",
        "https://images.unsplash.com/photo-1469398715555-76331a6e41c4",
        "https://images.unsplash.com/photo-1530847887473-7b9a3461268f",
        "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c",
        "https://images.unsplash.com/photo-1524253482453-3fed8d2fe12b",
        "https://images.unsplash.com/photo-1464666495445-5bc1f17ce7c4",
        "https://images.unsplash.com/photo-1424746219973-8fe3bd07d8e3",
        "https://images.unsplash.com/photo-1517841905240-472988babdf9",
    ],
    "Trouser": [
        "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c",
        "https://images.unsplash.com/photo-1491553895911-0055eca6402d",
        "https://images.unsplash.com/photo-1517263904808-5dc0d6e2eca0",
        "https://images.unsplash.com/photo-1520964099320-b7116d3a27c3",
        "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e",
        "https://images.unsplash.com/photo-1502378735452-bc7d86632805",
        "https://images.unsplash.com/photo-1416339306562-f3d12fefd36f",
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        "https://images.unsplash.com/photo-1465101046530-73398c7f28ca",
    ],
    "Watches": [
        "https://images.unsplash.com/photo-1434056886845-dac89ffe9b56",
        "https://images.unsplash.com/photo-1434056886845-dac89ffe9b56",
        "https://images.unsplash.com/photo-1519125323398-675f0ddb6308",
        "https://images.unsplash.com/photo-1469594292607-7bd90e0c2e43",
        "https://images.unsplash.com/photo-1465101162946-4377e57745c3",
        "https://images.unsplash.com/photo-1510797215324-95aa89f41c52",
        "https://images.unsplash.com/photo-1473187983305-f615310e7daa",
        "https://images.unsplash.com/photo-1519125323398-675f0ddb6308",
        "https://images.unsplash.com/photo-1519125323398-675f0ddb6308",
        "https://images.unsplash.com/photo-1519125323398-675f0ddb6308",
    ],
    "Shoes": [
        "https://images.unsplash.com/photo-1517263904808-5dc0d6e2eca0",
        "https://images.unsplash.com/photo-1526178613658-3c702bfc1c79",
        "https://images.unsplash.com/photo-1508739773434-c26b3d09e071",
        "https://images.unsplash.com/photo-1519864600265-abb224a442c9",
        "https://images.unsplash.com/photo-1519864600265-abb224a442c9",
        "https://images.unsplash.com/photo-1553342381-9aa8b07dca73",
        "https://images.unsplash.com/photo-1571731956672-643658ef2826",
        "https://images.unsplash.com/photo-1519864600265-abb224a442c9",
        "https://images.unsplash.com/photo-1484517186945-85072947a5d7",
        "https://images.unsplash.com/photo-1463100099107-aa0980c362e6",
    ],
}

PRODUCTS = {
    "Shirt": [
        {
            "name": f"Cricket Jersey {i + 1}",
            "price": 899 + i * 50,
            "size": ["S", "M", "L", "XL"][i % 4],
        } for i in range(10)
    ],
    "Trouser": [
        {
            "name": f"Jogger Trouser {i + 1}",
            "price": 1099 + i * 60,
            "size": ["28", "30", "32", "34", "36"][i % 5],
        } for i in range(10)
    ],
    "Watches": [
        {
            "name": f"Sports Watch {i + 1}",
            "price": 2499 + i * 100,
            "size": None,
        } for i in range(10)
    ],
    "Shoes": [
        {
            "name": f"Running Shoes {i + 1}",
            "price": 1799 + i * 120,
            "size": [f"{6 + (i % 5)}"],  # Sizes 6-10
        } for i in range(10)
    ],
}

# PUBLIC_INTERFACE
def seed_data(db: Session):
    """
    Completely purge all products and categories from the database.
    After operation, both the Product and Category tables will be empty.
    No products or categories are re-added.
    """
    # Delete all products
    db.query(models.Product).delete()
    db.commit()
    # Delete all categories
    db.query(models.Category).delete()
    db.commit()

