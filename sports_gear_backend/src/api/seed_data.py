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
    }
]


def seed_categories_and_products(db: Session):
    # Insert categories if missing
    for c in CATEGORIES:
        category = db.query(models.ProductCategory).filter_by(name=c['name']).first()
        if not category:
            category = models.ProductCategory(name=c['name'], description=c['description'])
            db.add(category)
            db.commit()
    db.commit()

    # Insert products if missing
    for item in PRODUCTS:
        # Get category object
        category = db.query(models.ProductCategory).filter_by(name=item['category_name']).first()
        if not category:
            continue
        # Check if product already exists for this name
        prod = db.query(models.Product).filter_by(name=item['name'], category_id=category.id).first()
        if prod:
            continue
        # Insert product
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
