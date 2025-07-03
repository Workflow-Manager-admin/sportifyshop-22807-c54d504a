import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from sports_gear_backend.src.api.models import Product
from sports_gear_backend.src.api.seed_data import get_db_session

# PUBLIC_INTERFACE
def seed_watches():
    """Seeds 10 watch products with names, descriptions, prices, and image URLs into the Product catalog."""
    db = get_db_session()
    watches = [
        {
            "name": "Speedster Chrono",
            "description": "A high-performance chronograph sports watch with water resistance and sleek steel look.",
            "price": 249.99,
            "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8"
        },
        {
            "name": "AeroRunner Digital",
            "description": "Lightweight digital sports watch with heart-rate monitor and step tracking, ideal for runners.",
            "price": 89.99,
            "image_url": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca"
        },
        {
            "name": "AquaDive Pro",
            "description": "Diver’s waterproof analog watch, luminous hands, and anti-scratch sapphire crystal face.",
            "price": 199.99,
            "image_url": "https://images.unsplash.com/photo-1519125323398-675f0ddb6308"
        },
        {
            "name": "PulseFit Smartwatch",
            "description": "Smartwatch with fitness tracking, notifications, and custom sport profiles.",
            "price": 129.95,
            "image_url": "https://images.unsplash.com/photo-1464983953574-0892a716854b"
        },
        {
            "name": "TrailBlazer Tough",
            "description": "Rugged outdoor GPS watch built for adventure, shock-resistant and solar powered.",
            "price": 179.50,
            "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb"
        },
        {
            "name": "UrbanSprint Minimal",
            "description": "Minimalist sports watch with soft silicone band, splash-proof, and bold look.",
            "price": 59.90,
            "image_url": "https://images.unsplash.com/photo-1522312346375-d1a52e2b99b3"
        },
        {
            "name": "Peak Performance Elite",
            "description": "Elite multi-sport training watch with altimeter, barometer, and compass.",
            "price": 249.00,
            "image_url": "https://images.unsplash.com/photo-1495106245174-55f3c4b27cde"
        },
        {
            "name": "Classic Endurance",
            "description": "Classic sports timepiece with leather band and precision quartz movement.",
            "price": 115.00,
            "image_url": "https://images.unsplash.com/photo-1454023492550-5696f8ff10e1"
        },
        {
            "name": "SprintTrack Wireless",
            "description": "Bluetooth-enabled sports watch with step, distance, and calorie tracking.",
            "price": 70.00,
            "image_url": "https://images.unsplash.com/photo-1465808883809-c7fd8bbb7a56"
        },
        {
            "name": "SunSport Hybrid",
            "description": "Hybrid analog-digital watch with solar charging for sustainable sport style.",
            "price": 139.99,
            "image_url": "https://images.unsplash.com/photo-1458057191847-70d96b8cd62d"
        },
    ]

    for watch in watches:
        # Check for duplicate
        exists = (
            db.query(Product)
            .filter(Product.name == watch["name"], Product.category == "watch")
            .first()
        )
        if not exists:
            product = Product(
                name=watch["name"],
                description=watch["description"],
                price=watch["price"],
                image_url=watch["image_url"],
                category="watch"
            )
            db.add(product)
    db.commit()
    print("Seeded 10 watch products successfully.")

if __name__ == "__main__":
    seed_watches()
