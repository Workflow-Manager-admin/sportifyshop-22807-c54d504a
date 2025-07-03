"""
Seed script for sports gear categories and products.

Seeds the database with a static set of sports gear categories and products,
with fixed names, public static image URLs, INR prices, and fixed available sizes.
Run idempotently and always ensures the same set of products are available in the catalog.

There are NO dynamic, real-time, or external updates—this remains constant across restarts.

After seeding, the /products endpoint always reflects the default set and values.
"""

from sqlalchemy.orm import Session
from . import models

# ------------------ STATIC DEFAULT CATEGORIES AND PRODUCTS ------------------

CATEGORIES = [
    {"name": "Shoes", "description": "Running, training, and sport-specific shoes"},
    {"name": "Balls", "description": "Footballs, basketballs, cricket, tennis, volleyball, and more"},
    {"name": "Apparel", "description": "Sports t-shirts, shorts, tracksuits, and gear"},
    {"name": "Equipment", "description": "Accessories and gear for sports and fitness"},
    {"name": "Bags", "description": "Sports bags and backpacks"},
    {"name": "Rackets", "description": "Badminton, tennis, squash rackets"},
    {"name": "Protective Gear", "description": "Helmets, pads, guards, mouthpieces, eyewear"},
    {"name": "Accessories", "description": "Socks, bottles, caps, wristbands, towels"},
    {"name": "Fitness", "description": "Home gym, weights, yoga, fitness tools"},
]

PRODUCTS = [
    # SHOES
    {
        "name": "Nike Revolution 6 Road Running Shoes",
        "description": "Men's lightweight running shoes for daily runs.",
        "image_url": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80",
        "price": 4599,
        "available_sizes": "UK7,UK8,UK9,UK10,UK11",
        "category_name": "Shoes",
    },
    {
        "name": "Adidas Predator Edge Football Boots",
        "description": "Durable turf shoes for pitch control.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/85/Adidas_Predator_Shoe_2016.jpg",
        "price": 3299,
        "available_sizes": "UK6,UK7,UK8,UK9,UK10",
        "category_name": "Shoes",
    },
    {
        "name": "Puma Softride Rift Running Shoes",
        "description": "Ultra-soft sports running shoes for men.",
        "image_url": "https://in.puma.com/media/catalog/product/3/7/377048_03_sv01.jpg",
        "price": 2999,
        "available_sizes": "UK5,UK6,UK7,UK8,UK9,UK10",
        "category_name": "Shoes",
    },
    # BALLS
    {
        "name": "Cosco Brasil Football Size-5",
        "description": "Quality football for every field.",
        "image_url": "https://m.media-amazon.com/images/I/614O6YGFQKL._SL1500_.jpg",
        "price": 749,
        "available_sizes": "5",
        "category_name": "Balls",
    },
    {
        "name": "Nivia Graffiti Basketball Size-7",
        "description": "Premium grip and bounce on all courts.",
        "image_url": "https://nivia.in/cdn/shop/products/333_Front_2.png?v=1626256981",
        "price": 840,
        "available_sizes": "7",
        "category_name": "Balls",
    },
    # APPAREL
    {
        "name": "Adidas Entrada 22 Jersey",
        "description": "Lightweight, moisture-absorbing sports jersey.",
        "image_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/f14815b2df1c42298436afc901304f96_9366/Entrada_22_Jersey_Red_H57566_01_laydown.jpg",
        "price": 1199,
        "available_sizes": "S,M,L,XL,XXL",
        "category_name": "Apparel",
    },
    {
        "name": "Nike Dri-FIT Academy Shorts",
        "description": "Breathable mesh shorts for training comfort.",
        "image_url": "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/afd5a1c2-8010-4c70-bea9-bd33606b6ade/challenger-2-in-1-7-running-shorts-0wJd9z.png",
        "price": 2195,
        "available_sizes": "S,M,L,XL",
        "category_name": "Apparel",
    },
    # EQUIPMENT
    {
        "name": "HEAD Pro Tennis Racket Overgrip",
        "description": "Superior grip and sweat absorption for rackets.",
        "image_url": "https://m.media-amazon.com/images/I/71c8mXJKKML._SL1500_.jpg",
        "price": 545,
        "available_sizes": "Standard",
        "category_name": "Equipment",
    },
    # BAGS
    {
        "name": "Wildcraft HypaDura Bolt Backpack",
        "description": "Multi-compartment backpack for sports gear.",
        "image_url": "https://www.wildcraft.com/media/catalog/product/cache/927c393b7777a39a877531d6b172c0be/1/1/11968_black-1.jpg",
        "price": 2650,
        "available_sizes": "Large",
        "category_name": "Bags",
    },
    # RACKETS
    {
        "name": "Yonex Nanoray 18i Badminton Racket",
        "description": "Superlight, fast head speed badminton racket.",
        "image_url": "https://m.media-amazon.com/images/I/718ePGTGo2L._SL1500_.jpg",
        "price": 2399,
        "available_sizes": "Standard",
        "category_name": "Rackets",
    },
    # PROTECTIVE GEAR
    {
        "name": "SG Cricket Batting Pads - Club",
        "description": "Lightweight, durable cricket pads.",
        "image_url": "https://m.media-amazon.com/images/I/81OudLwTx3L._SL1500_.jpg",
        "price": 1399,
        "available_sizes": "Men,Youth",
        "category_name": "Protective Gear",
    },
    # ACCESSORIES
    {
        "name": "Reebok Training Water Bottle",
        "description": "Durable BPA-free water bottle with twist cap.",
        "image_url": "https://assets.reebok.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/c1dbb7a0913d463193b6aa94011698d3_9366/TR_BOTTLE_600_GZ8636_01_standard.jpg",
        "price": 499,
        "available_sizes": "600ml",
        "category_name": "Accessories",
    },
    # FITNESS
    {
        "name": "Strauss Anti-Skid Yoga Mat",
        "description": "Lightweight, anti-slip, roll-up yoga mat.",
        "image_url": "https://m.media-amazon.com/images/I/71ULf9rKjxL._SL1500_.jpg",
        "price": 799,
        "available_sizes": "6mm,8mm",
        "category_name": "Fitness",
    },
]

# PUBLIC_INTERFACE
def seed_categories_and_products(db: Session):
    """
    PUBLIC_INTERFACE: Seed the sports gear categories and products with static, known-good data only.

    Seeds categories, then a fixed product set for each category. Skips duplicates on reruns.
    No dynamic fetching, no real-time/dynamic sources, no updates after initial seed.
    """
    # Insert all categories if missing
    name_to_cat = {}
    for c in CATEGORIES:
        category = db.query(models.ProductCategory).filter_by(name=c["name"]).first()
        if not category:
            category = models.ProductCategory(name=c["name"], description=c["description"])
            db.add(category)
            db.commit()
        name_to_cat[c["name"]] = category
    db.commit()
    # Insert products (unique by name+category), forcibly overwrite description/image/price/sizes
    for item in PRODUCTS:
        category = name_to_cat.get(item["category_name"])
        if not category:
            continue
        prod = db.query(models.Product).filter_by(name=item["name"], category_id=category.id).first()
        if prod:
            prod.description = item["description"]
            prod.image_url = item["image_url"]
            prod.price = float(item["price"])
            prod.available_sizes = item["available_sizes"]
            db.add(prod)
            db.commit()
            continue
        prod = models.Product(
            name=item["name"],
            description=item["description"],
            image_url=item["image_url"],
            price=float(item["price"]),
            available_sizes=item["available_sizes"],
            category_id=category.id,
        )
        db.add(prod)
        db.commit()
