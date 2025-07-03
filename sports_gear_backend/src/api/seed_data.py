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
        "image_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/87669b74e07244b9bef5ae5501238a3d_9366/Predator_Edge_4_Firm_Ground_Boots_Black_GW0972_01_standard.jpg",
        "price": 3299,
        "available_sizes": "UK6,UK7,UK8,UK9,UK10",
        "category_name": "Shoes",
    },
    {
        "name": "Puma Softride Rift Running Shoes",
        "description": "Ultra-soft sports running shoes for men.",
        "image_url": "https://images.puma.com/image/upload/f_auto,q_auto,b_rgb:fafafa,w_600,h_600/global/377048/03/sv01/fnd/IND/fmt/png/Softride-Rift-Men's-Running-Shoes",
        "price": 2999,
        "available_sizes": "UK5,UK6,UK7,UK8,UK9,UK10",
        "category_name": "Shoes",
    },
    # BALLS
    {
        "name": "Cosco Brasil Football Size-5",
        "description": "Quality football for every field.",
        "image_url": "https://static-01.daraz.pk/p/d65bb89ced4f09bb260101ef0ac63f1f.jpg",
        "price": 749,
        "available_sizes": "5",
        "category_name": "Balls",
    },
    {
        "name": "Nivia Graffiti Basketball Size-7",
        "description": "Premium grip and bounce on all courts.",
        "image_url": "https://rukminim2.flixcart.com/image/416/416/ke1pnrk0/basketball/i/b/a/7-2765graffitiorange-nivia-original-imafutkuss3uxqrv.jpeg",
        "price": 840,
        "available_sizes": "7",
        "category_name": "Balls",
    },
    # APPAREL
    {
        "name": "Adidas Entrada 22 Jersey",
        "description": "Lightweight, moisture-absorbing sports jersey.",
        "image_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/c9b851c802d04676a955afec0127853c_9366/Entrada_22_Jersey_White_H57564_01_laydown.jpg",
        "price": 1199,
        "available_sizes": "S,M,L,XL,XXL",
        "category_name": "Apparel",
    },
    {
        "name": "Nike Dri-FIT Academy Shorts",
        "description": "Breathable mesh shorts for training comfort.",
        "image_url": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/33e129b9115542d5b5b7f793c8e1a58a/dri-fit-academy-mens-soccer-shorts-xsKfsT.png",
        "price": 2195,
        "available_sizes": "S,M,L,XL",
        "category_name": "Apparel",
    },
    # EQUIPMENT
    {
        "name": "HEAD Pro Tennis Racket Overgrip",
        "description": "Superior grip and sweat absorption for rackets.",
        "image_url": "https://www.head.com/media/catalog/product/h/e/head-pro-overgrip-white-tennis-pack-3-overgrip-281704_wh.jpg",
        "price": 545,
        "available_sizes": "Standard",
        "category_name": "Equipment",
    },
    # BAGS
    {
        "name": "Wildcraft HypaDura Bolt Backpack",
        "description": "Multi-compartment backpack for sports gear.",
        "image_url": "https://wildcraftimages.s3.ap-south-1.amazonaws.com/img/bags/11968-black-2.jpg",
        "price": 2650,
        "available_sizes": "Large",
        "category_name": "Bags",
    },
    # RACKETS
    {
        "name": "Yonex Nanoray 18i Badminton Racket",
        "description": "Superlight, fast head speed badminton racket.",
        "image_url": "https://cdn.shopify.com/s/files/1/0618/7650/7113/products/yonex-nanoray-18i-badminton-racket-1.jpg",
        "price": 2399,
        "available_sizes": "Standard",
        "category_name": "Rackets",
    },
    # PROTECTIVE GEAR
    {
        "name": "SG Cricket Batting Pads - Club",
        "description": "Lightweight, durable cricket pads.",
        "image_url": "https://static-01.daraz.pk/p/570ad6f01220060da2939b16c046263e.jpg",
        "price": 1399,
        "available_sizes": "Men,Youth",
        "category_name": "Protective Gear",
    },
    # ACCESSORIES
    {
        "name": "Reebok Training Water Bottle",
        "description": "Durable BPA-free water bottle with twist cap.",
        "image_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto,fl_lossy,c_fill,g_auto/44e06e0a5c0344c3a409af920085dfa2_9366/Training_Water_Bottle_0.75_L_Blue_CF3522_01_standard.jpg",
        "price": 499,
        "available_sizes": "600ml",
        "category_name": "Accessories",
    },
    # FITNESS
    {
        "name": "Strauss Anti-Skid Yoga Mat",
        "description": "Lightweight, anti-slip, roll-up yoga mat.",
        "image_url": "https://5.imimg.com/data5/SELLER/Default/2023/8/337514916/KW/JT/CK/183243041/anti-skid-yoga-mat.jpg",
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
