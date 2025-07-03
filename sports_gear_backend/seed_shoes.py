import os
import sqlite3

# PUBLIC_INTERFACE
def seed_shoes(db_path=None):
    """Seeds the database with 10 shoe products, including names, prices, and image filenames."""
    if db_path is None:
        db_path = os.path.join(os.path.dirname(__file__), '..', 'sports_gear.db')

    shoes = [
        {
            "name": "Nike Air Zoom Pegasus",
            "description": "Lightweight running shoes with breathable mesh upper.",
            "price": 119.99,
            "image": "nike_pegasus.jpg",
            "category": "shoes",
            "sizes": "7,8,9,10,11"
        },
        {
            "name": "Adidas Ultraboost 21",
            "description": "High-cushion shoes ideal for long-distance running.",
            "price": 139.99,
            "image": "adidas_ultraboost.jpg",
            "category": "shoes",
            "sizes": "7,8,9,10,11,12"
        },
        {
            "name": "Puma Flyer Runner",
            "description": "Versatile everyday trainers for gym and track.",
            "price": 74.99,
            "image": "puma_flyer.jpg",
            "category": "shoes",
            "sizes": "6,7,8,9,10,11"
        },
        {
            "name": "Under Armour Charged Assert 9",
            "description": "Durable shoes with balance of flexibility and cushioning.",
            "price": 84.99,
            "image": "ua_assert.jpg",
            "category": "shoes",
            "sizes": "7,8,9,10,11,12,13"
        },
        {
            "name": "Asics Gel-Kayano 27",
            "description": "Supportive stability shoes with gel shock-absorption.",
            "price": 149.99,
            "image": "asics_kayano.jpg",
            "category": "shoes",
            "sizes": "8,9,10,11,12"
        },
        {
            "name": "Reebok Nano X1",
            "description": "Cross-training shoes designed for all workouts.",
            "price": 129.99,
            "image": "reebok_nano.jpg",
            "category": "shoes",
            "sizes": "6,7,8,9,10"
        },
        {
            "name": "New Balance Fresh Foam 1080v11",
            "description": "Premium neutral running shoes with plush cushioning.",
            "price": 159.99,
            "image": "nb_foam_1080.jpg",
            "category": "shoes",
            "sizes": "7,8,9,10,11"
        },
        {
            "name": "Saucony Ride 14",
            "description": "Smooth and energetic ride for daily runners.",
            "price": 114.99,
            "image": "saucony_ride14.jpg",
            "category": "shoes",
            "sizes": "8,9,10,11,12"
        },
        {
            "name": "Mizuno Wave Rider 25",
            "description": "Reliable performance shoes with responsive cushioning.",
            "price": 129.99,
            "image": "mizuno_waverider.jpg",
            "category": "shoes",
            "sizes": "7,8,9,10,12"
        },
        {
            "name": "Brooks Ghost 14",
            "description": "Soft and balanced shoes, great for roads and treadmills.",
            "price": 134.99,
            "image": "brooks_ghost.jpg",
            "category": "shoes",
            "sizes": "8,9,10,11"
        },
    ]

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Add the products table if it doesn't exist
    cur.execute('''CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        image TEXT,
        category TEXT,
        sizes TEXT
    )''')

    # Insert shoes data
    for shoe in shoes:
        cur.execute('''
            INSERT INTO products (name, description, price, image, category, sizes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (shoe['name'], shoe['description'], shoe['price'], shoe['image'], shoe['category'], shoe['sizes']))

    conn.commit()
    conn.close()
    print("Seeded 10 shoes successfully.")

if __name__ == "__main__":
    seed_shoes()
