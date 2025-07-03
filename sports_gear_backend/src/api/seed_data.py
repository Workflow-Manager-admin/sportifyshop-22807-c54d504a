"""
Seed script for sports gear categories and products.

On import, seeds the database with categories and realistic sports gear products
WITH real image URLs, realistic descriptions, sizes, and INR prices.

This file can be imported and called in startup_event in main.py.
"""

from sqlalchemy.orm import Session
from . import models

CATEGORIES = [
    {
        "name": "Shoes",
        "description": "Running, training, and sport-specific shoes"
    },
    {
        "name": "Balls",
        "description": "Footballs, basketballs, cricket and tennis balls"
    },
    {
        "name": "Apparel",
        "description": "Sports t-shirts, shorts, tracksuits, activewear"
    },
    {
        "name": "Equipment",
        "description": "Accessories and gear for sports and fitness"
    },
    {
        "name": "Bags",
        "description": "Sports bags and backpacks"
    },
    {
        "name": "Rackets",
        "description": "Badminton, tennis, and squash rackets"
    }
]
PRODUCTS = [
    # Shoes
    {
        "name": "Nike Revolution 6 Running Shoes",
        "description": "Lightweight running shoes with soft foam cushioning, perfect for daily runs.",
        "image_url": "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/c4c74f9732ae4e20af73679fd3e50c63/nike-revolution-6-road-running-shoes-8DcMTb.png",
        "price": 4599,
        "available_sizes": "UK7,UK8,UK9,UK10,UK11",
        "category_name": "Shoes"
    },
    {
        "name": "Adidas Predator Edge.4 Football Shoes",
        "description": "Durable and grippy outsole with synthetic upper for better ball control on the pitch.",
        "image_url": "https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/6081bdbbde7d4569813bac3c0117b5fc_9366/PREDATOR_EDGE.4_FG_GW2328_01_standard.jpg",
        "price": 3299,
        "available_sizes": "UK6,UK7,UK8,UK9,UK10",
        "category_name": "Shoes"
    },
    {
        "name": "ASICS GEL-QUANTUM 180 6",
        "description": "Gel cushioning for comfort during sports and training. Mesh upper for breathability.",
        "image_url": "https://images.asics.com/is/image/asics/1021A492_021_SR_RT_GLB?$sfcc-product$",
        "price": 7499,
        "available_sizes": "UK7,UK8,UK9,UK10,UK11",
        "category_name": "Shoes"
    },
    {
        "name": "Skechers Go Run Consistent",
        "description": "Responsive Ultra Go cushioning, mesh and synthetic upper for running comfort.",
        "image_url": "https://m.media-amazon.com/images/I/71qixD+h6uL._UL1500_.jpg",
        "price": 3290,
        "available_sizes": "UK6,UK7,UK8,UK9,UK10",
        "category_name": "Shoes"
    },
    # Balls
    {
        "name": "Nivia Shining Star Football",
        "description": "FIFA Inspected quality, excellent bounce, and durable synthetic material.",
        "image_url": "https://nivia.in/cdn/shop/products/395_Front_2.png?v=1626256871",
        "price": 899,
        "available_sizes": "5",
        "category_name": "Balls"
    },
    {
        "name": "Cosco Tournament Basketball",
        "description": "Made from high-quality rubber for extra grip and better durability.",
        "image_url": "https://m.media-amazon.com/images/I/81usfvEvFLL._SL1500_.jpg",
        "price": 749,
        "available_sizes": "7",
        "category_name": "Balls"
    },
    {
        "name": "SG Tournament Cricket Ball",
        "description": "Hand-stitched, waterproof four-piece cricket ball, official match quality.",
        "image_url": "https://m.media-amazon.com/images/I/71nT09bnYCL._SL1100_.jpg",
        "price": 430,
        "available_sizes": "Standard",
        "category_name": "Balls"
    },
    {
        "name": "Yonex Mavis 350 Badminton Shuttlecocks",
        "description": "Durable nylon shuttlecocks for professionals and amateurs.",
        "image_url": "https://m.media-amazon.com/images/I/61THTcFxx1L._SL1200_.jpg",
        "price": 815,
        "available_sizes": "Standard",
        "category_name": "Balls"
    },
    # Apparel
    {
        "name": "Puma Active Big Logo Tee",
        "description": "Moisture-wicking technology with big graphic print, ideal for workouts or casual wear.",
        "image_url": "https://in.puma.com/media/catalog/product/5/3/537224_01_mod01.jpg",
        "price": 1399,
        "available_sizes": "S,M,L,XL,XXL",
        "category_name": "Apparel"
    },
    {
        "name": "Nike Dri-FIT Challenger 2-in-1 Shorts",
        "description": "Versatile and sweat-wicking layered shorts for running and training.",
        "image_url": "https://static.nike.com/a/images/c_limit,w_592,f_auto/t_product_v1/afd5a1c2-8010-4c70-bea9-bd33606b6ade/challenger-2-in-1-7-running-shorts-0wJd9z.png",
        "price": 2195,
        "available_sizes": "S,M,L,XL",
        "category_name": "Apparel"
    },
    {
        "name": "Adidas Entrada 22 Jersey",
        "description": "Climalite fabric wicks sweat to keep you dry in the heat of battle.",
        "image_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/f14815b2df1c42298436afc901304f96_9366/Entrada_22_Jersey_Red_H57566_01_laydown.jpg",
        "price": 1199,
        "available_sizes": "S,M,L,XL,XXL",
        "category_name": "Apparel"
    },
    {
        "name": "SG Cricket Track Pants",
        "description": "Polyester track pants for comfort and agility on/off the pitch.",
        "image_url": "https://m.media-amazon.com/images/I/61rHk4npsBL._UL1200_.jpg",
        "price": 749,
        "available_sizes": "S,M,L,XL,XXL",
        "category_name": "Apparel"
    },
    # Equipment
    {
        "name": "HEAD Pro Tennis Racket Overgrip (3-pack)",
        "description": "Tacky, absorbent grip to enhance your racket control and feel.",
        "image_url": "https://m.media-amazon.com/images/I/71c8mXJKKML._SL1500_.jpg",
        "price": 545,
        "available_sizes": "Standard",
        "category_name": "Equipment"
    },
    {
        "name": "Cosco Resistance Tube Super",
        "description": "High-quality resistance tube for home workouts, strength and flexibility.",
        "image_url": "https://m.media-amazon.com/images/I/719JWe3B8mL._SL1500_.jpg",
        "price": 399,
        "available_sizes": "Standard",
        "category_name": "Equipment"
    },
    {
        "name": "GM Icon English Willow Cricket Bat",
        "description": "Grade 4 English Willow, lightweight with thick edges for power and control.",
        "image_url": "https://m.media-amazon.com/images/I/81PKt5NOJEL._SL1500_.jpg",
        "price": 4199,
        "available_sizes": "Standard",
        "category_name": "Equipment"
    },
    {
        "name": "Adidas Fitness Skipping Rope",
        "description": "Lightweight, adjustable skipping rope for cardio and HIIT workouts.",
        "image_url": "https://images.unsplash.com/photo-1517649763962-0c623066013b",
        "price": 799,
        "available_sizes": "Standard",
        "category_name": "Equipment"
    },
    # Bags
    {
        "name": "Wildcraft HypaDura Bolt Large Backpack",
        "description": "Spacious, water-resistant, multi-compartment backpack for all your gear.",
        "image_url": "https://www.wildcraft.com/media/catalog/product/cache/927c393b7777a39a877531d6b172c0be/1/1/11968_black-1.jpg",
        "price": 2699,
        "available_sizes": "L",
        "category_name": "Bags"
    },
    {
        "name": "Nike Brasilia Training Duffel Bag",
        "description": "Versatile sports duffel bag with plenty of room for your gear and a ventilated shoe compartment.",
        "image_url": "https://static.nike.com/a/images/t_prod/w_960,c_limit,f_auto/12b810e8-738d-4799-a6d8-2ec3e897e0f8/brasilia-small-training-duffel-bag-JnWbG5.png",
        "price": 1895,
        "available_sizes": "Medium,Large",
        "category_name": "Bags"
    },
    {
        "name": "Vivo IPL Cricket Kit Bag",
        "description": "Professional-grade kit bag featuring multiple compartments, waterproof base, and padded straps.",
        "image_url": "https://m.media-amazon.com/images/I/71jlEVdJ61L._SL1500_.jpg",
        "price": 1899,
        "available_sizes": "XL",
        "category_name": "Bags"
    },
    {
        "name": "Yonex Team Tennis 6 Racket Bag",
        "description": "Spacious bag for up to 6 rackets, heavy-duty fabric, stylish design.",
        "image_url": "https://m.media-amazon.com/images/I/81g6XJY3qgL._SL1500_.jpg",
        "price": 2659,
        "available_sizes": "Large",
        "category_name": "Bags"
    },
    # Rackets
    {
        "name": "Yonex Nanoray 18i Graphite Badminton Racket",
        "description": "Superlight graphite racquet for fast and controlled play. Includes full cover.",
        "image_url": "https://m.media-amazon.com/images/I/718ePGTGo2L._SL1500_.jpg",
        "price": 2399,
        "available_sizes": "Standard",
        "category_name": "Rackets"
    },
    {
        "name": "Wilson Pro Staff Team Tennis Racket",
        "description": "Iconic design, lightweight graphite, perfect for aggressive play.",
        "image_url": "https://m.media-amazon.com/images/I/81-4wliirnL._SL1500_.jpg",
        "price": 7990,
        "available_sizes": "Standard",
        "category_name": "Rackets"
    },
    {
        "name": "Li-Ning Ultra Strong 9500 Plus Badminton Racket",
        "description": "Superb control and lightweight for rapid strokes; carbon fiber construction.",
        "image_url": "https://m.media-amazon.com/images/I/81RZe2pHoXL._SL1500_.jpg",
        "price": 2840,
        "available_sizes": "Standard",
        "category_name": "Rackets"
    },
    {
        "name": "Slazenger V1000 Hockey Stick",
        "description": "Fiberglass reinforced composite, lightweight and powerful for field hockey.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/11/Slazenger_Hockey_Stick_%2812898642143%29.jpg",
        "price": 2350,
        "available_sizes": "36.5\",37.5\"",
        "category_name": "Rackets"
    }
]


def seed_categories_and_products(db: Session):
    """
    Seeds the sports gear categories and products with real image URLs, INR prices, and appropriate sizes/categories,
    only if they do not already exist. Makes data available to the /products endpoint in real time.

    Args:
        db (Session): SQLAlchemy database session.
    """
    # Insert categories if missing
    for c in CATEGORIES:
        category = db.query(models.ProductCategory).filter_by(name=c['name']).first()
        if not category:
            category = models.ProductCategory(name=c['name'], description=c['description'])
            db.add(category)
            db.commit()
    db.commit()

    # Insert products if missing (avoid duplication)
    for item in PRODUCTS:
        category = db.query(models.ProductCategory).filter_by(name=item['category_name']).first()
        if not category:
            continue
        prod = db.query(models.Product).filter_by(name=item['name'], category_id=category.id).first()
        # Correction: If product exists but image_url is missing or altered, or not a valid public url, update it.
        if prod:
            # Check for valid http(s) image_url, update if existing is empty or not starting with http
            correct_url = item['image_url']
            update_needed = False
            if not prod.image_url or not (prod.image_url.startswith("http://") or prod.image_url.startswith("https://")):
                update_needed = True
            elif correct_url and prod.image_url != correct_url:
                update_needed = True
            if update_needed:
                prod.image_url = correct_url
                db.add(prod)
                db.commit()
            continue
        prod = models.Product(
            name=item['name'],
            description=item['description'],
            image_url=item['image_url'],
            price=float(item['price']),
            available_sizes=item['available_sizes'],
            category_id=category.id
        )
        db.add(prod)
    db.commit()
