"""
Seed script to add 10 trousers products with images and prices to the product catalog.
Usage: python seed_trousers.py
"""

import os
import sys
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "sports_gear.db")

TROUSERS_PRODUCTS = [
    {
        "name": "Classic Black Sports Trousers",
        "description": "Versatile and stylish black sports trousers. Breathable fabric, suitable for all activities.",
        "price": 39.99,
        "image_url": "/uploaded_images/trousers_black_classic.jpg",
        "category": "trousers",
        "sizes": "S,M,L,XL"
    },
    {
        "name": "Running Blue Track Pants",
        "description": "Lightweight blue track pants for optimal running comfort.",
        "price": 34.99,
        "image_url": "/uploaded_images/trousers_blue_track.jpg",
        "category": "trousers",
        "sizes": "S,M,L,XL"
    },
    {
        "name": "Grey Slim Fit Trousers",
        "description": "Modern fit, premium-quality grey trousers ideal for gym or casual wear.",
        "price": 42.5,
        "image_url": "/uploaded_images/trousers_grey_slim.jpg",
        "category": "trousers",
        "sizes": "XS,S,M,L"
    },
    {
        "name": "Classic White Joggers",
        "description": "Comfortable white joggers with adjustable drawstring.",
        "price": 31.99,
        "image_url": "/uploaded_images/trousers_white_joggers.jpg",
        "category": "trousers",
        "sizes": "M,L,XL"
    },
    {
        "name": "Red Performance Trousers",
        "description": "Bold red performance trousers for stylish training sessions.",
        "price": 44.99,
        "image_url": "/uploaded_images/trousers_red_performance.jpg",
        "category": "trousers",
        "sizes": "S,M,L,XXL"
    },
    {
        "name": "Dark Green Cargo Pants",
        "description": "Multi-pocket cargo pants, ideal for outdoors and training.",
        "price": 47.99,
        "image_url": "/uploaded_images/trousers_green_cargo.jpg",
        "category": "trousers",
        "sizes": "L,XL,XXL"
    },
    {
        "name": "Classic Navy Joggers",
        "description": "Navy blue joggers with soft inner lining for maximum comfort.",
        "price": 37.99,
        "image_url": "/uploaded_images/trousers_navy_joggers.jpg",
        "category": "trousers",
        "sizes": "S,M,L"
    },
    {
        "name": "Grey Melange Tights",
        "description": "Snug-fit melange tights for workouts and yoga.",
        "price": 28.99,
        "image_url": "/uploaded_images/trousers_grey_melange.jpg",
        "category": "trousers",
        "sizes": "XS,S,M,L"
    },
    {
        "name": "Olive Green Flex Pants",
        "description": "Stretchy olive green pants for training and athleisure.",
        "price": 38.5,
        "image_url": "/uploaded_images/trousers_olive_flex.jpg",
        "category": "trousers",
        "sizes": "M,L,XL"
    },
    {
        "name": "Urban Camo Training Trousers",
        "description": "Trendy camo trousers designed for urban workouts.",
        "price": 45.0,
        "image_url": "/uploaded_images/trousers_camo_training.jpg",
        "category": "trousers",
        "sizes": "S,M,L,XL,XXL"
    },
]

def seed_trousers(db_path: str = DB_PATH):
    """
    Inserts 10 trousers products into the sports_gear database.
    """
    print(f"Connecting to database at {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create products table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        image_url TEXT,
        category TEXT,
        sizes TEXT
    )
    """)

    # Check if trousers already exist
    cursor.execute("SELECT COUNT(*) FROM products WHERE category = ?", ("trousers",))
    existing_count = cursor.fetchone()[0]

    if existing_count >= 10:
        print("At least 10 trousers products already exist, skipping seeding.")
        conn.close()
        return

    print(f"Adding {10 - existing_count} trousers products.")
    for trouser in TROUSERS_PRODUCTS:
        cursor.execute(
            "INSERT INTO products (name, description, price, image_url, category, sizes) VALUES (?, ?, ?, ?, ?, ?)",
            (
                trouser["name"],
                trouser["description"],
                trouser["price"],
                trouser["image_url"],
                trouser["category"],
                trouser["sizes"],
            ),
        )

    conn.commit()
    conn.close()
    print("Seeding trousers completed.")

if __name__ == "__main__":
    seed_trousers()
