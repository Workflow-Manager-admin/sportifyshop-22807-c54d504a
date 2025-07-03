"""
Seed script for sports gear categories and products.

Seeds the database with a diverse, realistic set of sports gear categories and products,
with unique names, real brand associations, accurate INR prices, and public image URLs.
Images are Open-licensed (official, unsplash, wikimedia, or manufacturer-hosted where allowed for illustration).
Each product has appropriate size/options and strong association with a properly-created category.

This runs idempotently and does not create duplicates on repeated runs.
"""

from sqlalchemy.orm import Session
from . import models

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
        "description": "Men's lightweight, soft-cushion running shoes for daily runners.",
        "image_url": "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/c4c74f9732ae4e20af73679fd3e50c63/nike-revolution-6-road-running-shoes-8DcMTb.png",
        "price": 4599,
        "available_sizes": "UK7,UK8,UK9,UK10,UK11",
        "category_name": "Shoes",
    },
    {
        "name": "Adidas Predator Edge.4 Football Boots",
        "description": "Durable turf shoes with synthetic upper for outstanding ball control.",
        "image_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/1e85c7220ba44dde8b92ad1800a2997d_9366/PREDATOR_EDGE.4_FG_GW2328_01_standard.jpg",
        "price": 3299,
        "available_sizes": "UK6,UK7,UK8,UK9,UK10",
        "category_name": "Shoes",
    },
    {
        "name": "Puma Softride Rift Running Shoes",
        "description": "Ultra-soft and plush for all-day wear, training, or walking.",
        "image_url": "https://in.puma.com/media/catalog/product/3/7/377048_03_sv01.jpg",
        "price": 2999,
        "available_sizes": "UK5,UK6,UK7,UK8,UK9,UK10",
        "category_name": "Shoes",
    },
    # BALLS
    {
        "name": "Cosco Brasil Football Size-5",
        "description": "Match-quality football. Hand-sewn, vibrant colours, designed for all surfaces.",
        "image_url": "https://m.media-amazon.com/images/I/614O6YGFQKL._SL1500_.jpg",
        "price": 749,
        "available_sizes": "5",
        "category_name": "Balls",
    },
    {
        "name": "Nivia Graffiti Basketball Orange Size-7",
        "description": "Premium rubber cover for superior grip and bounce on indoor/outdoor courts.",
        "image_url": "https://nivia.in/cdn/shop/products/333_Front_2.png?v=1626256981",
        "price": 840,
        "available_sizes": "7",
        "category_name": "Balls",
    },
    {
        "name": "SG Club Leather Cricket Ball",
        "description": "Hand-stitched four-piece ball for club level play; waterproof and durable.",
        "image_url": "https://4.imimg.com/data4/YX/PH/GLADMIN-/sg-club-500x500.jpg",
        "price": 410,
        "available_sizes": "Standard",
        "category_name": "Balls",
    },
    {
        "name": "Yonex Mavis 350 Shuttlecocks (Pack of 6)",
        "description": "Durable, tournament-grade nylon shuttlecocks for all levels.",
        "image_url": "https://m.media-amazon.com/images/I/61THTcFxx1L._SL1200_.jpg",
        "price": 825,
        "available_sizes": "Standard",
        "category_name": "Balls",
    },
    # APPAREL
    {
        "name": "Adidas Entrada 22 Jersey",
        "description": "Moisture-absorbing AEROREADY fabric keeps you dry during intense play.",
        "image_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/f14815b2df1c42298436afc901304f96_9366/Entrada_22_Jersey_Red_H57566_01_laydown.jpg",
        "price": 1199,
        "available_sizes": "S,M,L,XL,XXL",
        "category_name": "Apparel",
    },
    {
        "name": "Nike Dri-FIT Academy Shorts",
        "description": "Breathable mesh, drawcord-adjustable waist—built for training and match comfort.",
        "image_url": "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/afd5a1c2-8010-4c70-bea9-bd33606b6ade/challenger-2-in-1-7-running-shorts-0wJd9z.png",
        "price": 2195,
        "available_sizes": "S,M,L,XL",
        "category_name": "Apparel",
    },
    {
        "name": "Puma Active Big Logo Tee",
        "description": "Moisture-wicking tee with bold logo for workout or casual style.",
        "image_url": "https://in.puma.com/media/catalog/product/5/3/537224_01_mod01.jpg",
        "price": 1350,
        "available_sizes": "S,M,L,XL,XXL",
        "category_name": "Apparel",
    },
    # EQUIPMENT
    {
        "name": "HEAD Pro Tennis Racket Overgrip",
        "description": "Superior grip and sweat absorption, pack of 3 for all racket types.",
        "image_url": "https://m.media-amazon.com/images/I/71c8mXJKKML._SL1500_.jpg",
        "price": 545,
        "available_sizes": "Standard",
        "category_name": "Equipment",
    },
    {
        "name": "Cosco Resistance Tube Super",
        "description": "Durable resistance tube for strength, flexibility, and rehab exercises.",
        "image_url": "https://m.media-amazon.com/images/I/719JWe3B8mL._SL1500_.jpg",
        "price": 399,
        "available_sizes": "Standard",
        "category_name": "Equipment",
    },
    {
        "name": "GM Icon English Willow Bat",
        "description": "Grade 4 English Willow, lightweight and powerful for quick strokes.",
        "image_url": "https://m.media-amazon.com/images/I/81PKt5NOJEL._SL1500_.jpg",
        "price": 3990,
        "available_sizes": "Full,Short Handle",
        "category_name": "Equipment",
    },
    # BAGS
    {
        "name": "Wildcraft HypaDura Bolt Backpack",
        "description": "Spacious multi-compartment, water-resistant, snug-fit for sports enthusiasts.",
        "image_url": "https://www.wildcraft.com/media/catalog/product/cache/927c393b7777a39a877531d6b172c0be/1/1/11968_black-1.jpg",
        "price": 2650,
        "available_sizes": "Large",
        "category_name": "Bags",
    },
    {
        "name": "Nike Brasilia Training Duffel",
        "description": "Versatile duffel for gym and travel, spacious, with ventilated compartments.",
        "image_url": "https://static.nike.com/a/images/t_prod/w_960,c_limit,f_auto/12b810e8-738d-4799-a6d8-2ec3e897e0f8/brasilia-small-training-duffel-bag-JnWbG5.png",
        "price": 1895,
        "available_sizes": "Medium,Large",
        "category_name": "Bags",
    },
    # RACKETS
    {
        "name": "Yonex Nanoray 18i Badminton Racket",
        "description": "Superlight graphite construction, fast head speed, full cover included.",
        "image_url": "https://m.media-amazon.com/images/I/718ePGTGo2L._SL1500_.jpg",
        "price": 2399,
        "available_sizes": "Standard",
        "category_name": "Rackets",
    },
    {
        "name": "Wilson Pro Staff Team Tennis Racket",
        "description": "Iconic control-oriented racket for intermediate/advanced tennis players.",
        "image_url": "https://m.media-amazon.com/images/I/81-4wliirnL._SL1500_.jpg",
        "price": 7990,
        "available_sizes": "Standard",
        "category_name": "Rackets",
    },
    # PROTECTIVE GEAR
    {
        "name": "SG Cricket Batting Pads - Club",
        "description": "Lightweight, durable pads for confident cricket batting, fastened with secure straps.",
        "image_url": "https://m.media-amazon.com/images/I/81OudLwTx3L._SL1500_.jpg",
        "price": 1399,
        "available_sizes": "Men,Youth",
        "category_name": "Protective Gear",
    },
    {
        "name": "Nivia Football Shin Guards",
        "description": "Ergonomic shell, EVA cushioning for impact absorption on soccer pitch.",
        "image_url": "https://nivia.in/cdn/shop/products/Hard_Shield_Shinguard_-_Front_1.png?v=1653471517",
        "price": 299,
        "available_sizes": "S,M,L",
        "category_name": "Protective Gear",
    },
    {
        "name": "Cosco Smash Vision Squash Eyewear",
        "description": "Anti-fog safety eyewear with clear lens for squash or racquetball.",
        "image_url": "https://m.media-amazon.com/images/I/615T-OfmYfL._SL1200_.jpg",
        "price": 825,
        "available_sizes": "Standard",
        "category_name": "Protective Gear",
    },
    # ACCESSORIES
    {
        "name": "Reebok Training Water Bottle",
        "description": "Durable BPA-free water bottle, twist cap, sports design.",
        "image_url": "https://assets.reebok.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/c1dbb7a0913d463193b6aa94011698d3_9366/TR_BOTTLE_600_GZ8636_01_standard.jpg",
        "price": 499,
        "available_sizes": "600ml",
        "category_name": "Accessories",
    },
    {
        "name": "Yonex Sports Wristband Pack",
        "description": "Highly absorbent, soft cotton wristbands with Yonex logo.",
        "image_url": "https://m.media-amazon.com/images/I/51RC1duNmQL._SL1200_.jpg",
        "price": 295,
        "available_sizes": "One Size",
        "category_name": "Accessories",
    },
    {
        "name": "SG Elite Bat Grip",
        "description": "Textured cricket bat grip for improved hold, pack of 2.",
        "image_url": "https://m.media-amazon.com/images/I/81O03OgOeQL._SL1500_.jpg",
        "price": 199,
        "available_sizes": "Standard",
        "category_name": "Accessories",
    },
    # FITNESS
    {
        "name": "Strauss Anti-Skid Yoga Mat",
        "description": "Lightweight anti-slip yoga mat. Roll-up and washable.",
        "image_url": "https://m.media-amazon.com/images/I/71ULf9rKjxL._SL1500_.jpg",
        "price": 799,
        "available_sizes": "6mm,8mm",
        "category_name": "Fitness",
    },
    {
        "name": "Bodygrip Adjustable Dumbbells (Pair)",
        "description": "Metal dumbbells with secure grip, adjustable up to 10kg.",
        "image_url": "https://m.media-amazon.com/images/I/71v7m2-LruL._SL1500_.jpg",
        "price": 2149,
        "available_sizes": "10kg,15kg",
        "category_name": "Fitness",
    },
    {
        "name": "Kobo Foam Roller Black",
        "description": "Relieve muscle soreness, portable foam roller for fitness recovery.",
        "image_url": "https://m.media-amazon.com/images/I/81nC8lQD0nL._SL1500_.jpg",
        "price": 889,
        "available_sizes": "33cm",
        "category_name": "Fitness",
    },
]

def seed_categories_and_products(db: Session):
    """
    Seeds the sports gear categories and products with public image URLs, INR prices,
    and appropriate sizes/categories, only if they do not already exist.
    Makes data available to /products for catalog endpoints.
    Skips duplicate creation on repeated startup.
    """
    # Insert ALL categories if missing
    name_to_cat = {}
    for c in CATEGORIES:
        category = db.query(models.ProductCategory).filter_by(name=c["name"]).first()
        if not category:
            category = models.ProductCategory(name=c["name"], description=c["description"])
            db.add(category)
            db.commit()
        name_to_cat[c["name"]] = category
    db.commit()
    # Insert products (unique by name+category), update image/price/size if mismatch
    for item in PRODUCTS:
        category = name_to_cat.get(item["category_name"])
        if not category:
            continue
        prod = db.query(models.Product).filter_by(name=item["name"], category_id=category.id).first()
        update_fields = {}
        if prod:
            # Update image_url, price, or sizes if changed or missing
            if not prod.image_url or prod.image_url != item["image_url"]:
                update_fields["image_url"] = item["image_url"]
            if prod.price != float(item["price"]):
                update_fields["price"] = float(item["price"])
            if prod.available_sizes != item["available_sizes"]:
                update_fields["available_sizes"] = item["available_sizes"]
            if update_fields:
                for k, v in update_fields.items():
                    setattr(prod, k, v)
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
