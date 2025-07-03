"""
Seed categories and sports gear products for the backend database.

- Removes all old products before seeding.
- Ensures categories exist.
- Adds 10 shirts, 10 trousers, 10 watches, and 10 shoes (with images/prices).
- Images use free stock links (pexels/unsplash).
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
    Uses unique, valid free stock images and realistic product details.
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

    # -- IMAGES SRC via Unsplash/Pexels (royalty-free, different for every product) --
    shoes_images = [
        "https://images.pexels.com/photos/19090/pexels-photo.jpg",  # white running shoes
        "https://images.unsplash.com/photo-1517260911205-8fbcd101ebb9",  # black sport shoes
        "https://images.pexels.com/photos/2529148/pexels-photo-2529148.jpeg",
        "https://images.pexels.com/photos/51342/pexels-photo-51342.jpeg",
        "https://images.unsplash.com/photo-1528701800484-9056baa27f6b",
        "https://images.pexels.com/photos/161097/sneakers-shoes-colorful-shoelaces-161097.jpeg",
        "https://images.unsplash.com/photo-1457979185131-c3770ff0a127",
        "https://images.pexels.com/photos/92028/pexels-photo-92028.jpeg",
        "https://images.unsplash.com/photo-1519864600265-abb23847ef2c",
        "https://images.pexels.com/photos/163365/sneakers-shoes-footwear-close-up-163365.jpeg",
    ]
    shirts_images = [
        "https://images.pexels.com/photos/298842/pexels-photo-298842.jpeg",
        "https://images.pexels.com/photos/1707823/pexels-photo-1707823.jpeg",
        "https://images.pexels.com/photos/2983464/pexels-photo-2983464.jpeg",
        "https://images.pexels.com/photos/532220/pexels-photo-532220.jpeg",
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        "https://images.pexels.com/photos/449406/pexels-photo-449406.jpeg",
        "https://images.unsplash.com/photo-1526178613658-3dbd69aa4b89",
        "https://images.pexels.com/photos/936075/pexels-photo-936075.jpeg",
        "https://images.pexels.com/photos/2983463/pexels-photo-2983463.jpeg",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
    ]
    trousers_images = [
        "https://images.pexels.com/photos/2983465/pexels-photo-2983465.jpeg",
        "https://images.pexels.com/photos/936094/pexels-photo-936094.jpeg",
        "https://images.pexels.com/photos/704219/pexels-photo-704219.jpeg",
        "https://images.pexels.com/photos/936100/pexels-photo-936100.jpeg",
        "https://images.unsplash.com/photo-1518611012118-696072aa579a",
        "https://images.pexels.com/photos/1804516/pexels-photo-1804516.jpeg",
        "https://images.pexels.com/photos/631160/pexels-photo-631160.jpeg",
        "https://images.unsplash.com/photo-1484517186945-948d2b3eaf6d",
        "https://images.pexels.com/photos/2983461/pexels-photo-2983461.jpeg",
        "https://images.unsplash.com/photo-1464983953574-0892a716854b",
    ]
    watches_images = [
        "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b",
        "https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg",
        "https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg",
        "https://images.unsplash.com/photo-1465101046530-73398c7f28ca",
        "https://images.pexels.com/photos/168575/pexels-photo-168575.jpeg",
        "https://images.unsplash.com/photo-1453411585723-503a1b4777e5",
        "https://images.pexels.com/photos/277319/pexels-photo-277319.jpeg",
        "https://images.unsplash.com/photo-1518461399624-5092a2c06c41",
        "https://images.pexels.com/photos/717549/pexels-photo-717549.jpeg",
        "https://images.pexels.com/photos/461062/pexels-photo-461062.jpeg",
    ]

    # 10 Shoes (Brand, style, price, sizes)
    for i in range(10):
        demo_products.append({
            "name": f"RunMax Sprint {i+1} Shoes",
            "description": (
                f"Performance running shoe, breathable mesh with anti-slip rubber. "
                f"Comfort and durability for long runs. Style {i+1}."
            ),
            "image_url": shoes_images[i],
            "price": 69.99 + i * 6.75,
            "available_sizes": "7,8,9,10,11,12",
            "category_name": "Shoes"
        })

    # 10 Shirts (poly/cotton, summer, dry-fit, crewneck, v-neck)
    for i in range(10):
        shirt_type = ["Crewneck Tee", "V-neck Tee", "Sleeveless Tank", "Performance Polo", "Compression Shirt",
                      "Cotton Tee", "Seamless Tee", "Jersey", "Base Layer", "Raglan Tee"][i]
        demo_products.append({
            "name": f"ActiveFlex {shirt_type} {i+1}",
            "description": (
                f"Lightweight, moisture-wicking sports shirt ({shirt_type}) for training and outdoor use. "
                f"Odor/fade-resistant, four-way stretch. Style {i+1}."
            ),
            "image_url": shirts_images[i],
            "price": 22.50 + i * 3.10,
            "available_sizes": "S,M,L,XL,XXL",
            "category_name": "Shirts"
        })

    # 10 Trousers (shorts, leggings, joggers, stretch)
    for i in range(10):
        trouser_type = ["Track Pants", "Training Shorts", "Compression Leggings", "Joggers", "Cargo Shorts",
                        "Slim Fit Pants", "Sport Capris", "Thermal Pants", "Summer Shorts", "Stretch Trousers"][i]
        demo_products.append({
            "name": f"MovePro {trouser_type} {i+1}",
            "description": (
                f"Flexible {trouser_type} for versatile sports activities. "
                f"Breathable fabric with adjustable waist. Style {i+1}."
            ),
            "image_url": trousers_images[i],
            "price": 27.99 + i * 2.40,
            "available_sizes": "S,M,L,XL,XXL",
            "category_name": "Trousers"
        })

    # 10 Watches (sport, GPS, digital, waterproof)
    for i in range(10):
        watch_type = ["Digital Chrono", "Fitness Tracker", "Smartwatch", "Running GPS Watch", "Waterproof Sport Watch",
                      "Classic Analog", "Digital Fitness", "Multisport Watch", "Pulse Watch", "Activity Smartwatch"][i]
        demo_products.append({
            "name": f"PulseSync {watch_type} {i+1}",
            "description": (
                f"Reliable sports watch: features {watch_type.lower()}, durable, splash resistant. "
                f"Stay on track with workout metrics or timekeeping. Style {i+1}."
            ),
            "image_url": watches_images[i],
            "price": 55.00 + i * 10.75,
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
    from .models import get_engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
    db = SessionLocal()
    seed_categories_and_products(db)
