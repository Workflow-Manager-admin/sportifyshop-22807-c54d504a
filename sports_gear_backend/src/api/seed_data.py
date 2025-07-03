"""
Seed script for Men's Apparel and Accessories categories and products.
Seeds only the following categories: Shirts, Trousers, Jackets, Shoes, Belts, Wallets, Watches, Ties, Sunglasses, Hats.
Each category has at least 10 unique products, with realistic INR prices, available sizes (when relevant), public image URLs, and descriptive details.
All sports categories/products are removed.
"""

from sqlalchemy.orm import Session
from . import models

CATEGORIES = [
    {"name": "Shirts", "description": "Men's shirts for all occasions"},
    {"name": "Trousers", "description": "Stylish and comfortable men's trousers"},
    {"name": "Jackets", "description": "Trendy men's jackets"},
    {"name": "Shoes", "description": "Men's footwear for work and leisure"},
    {"name": "Belts", "description": "Men's leather and fabric belts"},
    {"name": "Wallets", "description": "Classic and contemporary men's wallets"},
    {"name": "Watches", "description": "Men's analog and digital watches"},
    {"name": "Ties", "description": "Formal and semi-formal men's ties"},
    {"name": "Sunglasses", "description": "Men's sunglasses for style and protection"},
    {"name": "Hats", "description": "Men's hats and caps for sun and fashion"},
]

# Public Image URLs (Unsplash, Pixabay, Pexels, etc.), can be reused/rotated
IMAGES = {
    "Shirts": [
        "https://images.pexels.com/photos/298863/pexels-photo-298863.jpeg",
        "https://images.unsplash.com/photo-1503342452485-86a096e77d79",
        "https://images.pexels.com/photos/220887/pexels-photo-220887.jpeg",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        "https://images.pexels.com/photos/2983464/pexels-photo-2983464.jpeg",
        "https://images.unsplash.com/photo-1519750157634-bbb07f2d7c92",
        "https://images.pexels.com/photos/532220/pexels-photo-532220.jpeg",
        "https://images.unsplash.com/photo-1515984979728-cb7b4a2d1d1c",
        "https://images.pexels.com/photos/936075/pexels-photo-936075.jpeg",
        "https://images.pexels.com/photos/428340/pexels-photo-428340.jpeg",
    ],
    "Trousers": [
        "https://images.pexels.com/photos/2988632/pexels-photo-2988632.jpeg",
        "https://images.unsplash.com/photo-1469398715555-76331d870b1d",
        "https://images.pexels.com/photos/1707828/pexels-photo-1707828.jpeg",
        "https://images.pexels.com/photos/2983467/pexels-photo-2983467.jpeg",
        "https://images.unsplash.com/photo-1465188162913-8a1049b2a8ff",
        "https://images.pexels.com/photos/385997/pexels-photo-385997.jpeg",
        "https://images.pexels.com/photos/169783/pexels-photo-169783.jpeg",
        "https://images.unsplash.com/photo-1519864600265-abb23847ef2c",
        "https://images.pexels.com/photos/428361/pexels-photo-428361.jpeg",
        "https://images.pexels.com/photos/321576/pexels-photo-321576.jpeg",
    ],
    "Jackets": [
        "https://images.unsplash.com/photo-1552374196-c4e7ffc6e126",
        "https://images.pexels.com/photos/936098/pexels-photo-936098.jpeg",
        "https://images.unsplash.com/photo-1491553895911-0055eca6402d",
        "https://images.pexels.com/photos/285173/pexels-photo-285173.jpeg",
        "https://images.pexels.com/photos/428319/pexels-photo-428319.jpeg",
        "https://images.unsplash.com/photo-1513648077-8bfa3ec94421",
        "https://images.pexels.com/photos/247917/pexels-photo-247917.jpeg",
        "https://images.unsplash.com/photo-1517841905240-472988babdf9",
        "https://images.pexels.com/photos/936094/pexels-photo-936094.jpeg",
        "https://images.pexels.com/photos/428340/pexels-photo-428340.jpeg",
    ],
    "Shoes": [
        "https://images.unsplash.com/photo-1519864600265-abb23847ef2c",
        "https://images.pexels.com/photos/19090/pexels-photo.jpg",
        "https://images.unsplash.com/photo-1517263904808-5dc0d07fe126",
        "https://images.pexels.com/photos/267202/pexels-photo-267202.jpeg",
        "https://images.unsplash.com/photo-1528701800484-9057b43c3cb0",
        "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c",
        "https://images.pexels.com/photos/2988635/pexels-photo-2988635.jpeg",
        "https://images.pexels.com/photos/267242/pexels-photo-267242.jpeg",
        "https://images.pexels.com/photos/200311/pexels-photo-200311.jpeg",
        "https://images.unsplash.com/photo-1513104890138-7c749659a591",
    ],
    "Belts": [
        "https://images.pexels.com/photos/2988634/pexels-photo-2988634.jpeg",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        "https://images.pexels.com/photos/2983460/pexels-photo-2983460.jpeg",
        "https://images.unsplash.com/photo-1515984979728-cb7b4a2d1d1c",
        "https://images.pexels.com/photos/346748/pexels-photo-346748.jpeg",
        "https://images.pexels.com/photos/1707828/pexels-photo-1707828.jpeg",
        "https://images.unsplash.com/photo-1519750157634-bbb07f2d7c92",
        "https://images.pexels.com/photos/325876/pexels-photo-325876.jpeg",
        "https://images.unsplash.com/photo-1464983953574-0892a716854b",
        "https://images.pexels.com/photos/934070/pexels-photo-934070.jpeg",
    ],
    "Wallets": [
        "https://images.pexels.com/photos/2988631/pexels-photo-2988631.jpeg",
        "https://images.unsplash.com/photo-1519750157634-bbb07f2d7c92",
        "https://images.pexels.com/photos/2983466/pexels-photo-2983466.jpeg",
        "https://images.pexels.com/photos/1707828/pexels-photo-1707828.jpeg",
        "https://images.pexels.com/photos/267202/pexels-photo-267202.jpeg",
        "https://images.pexels.com/photos/934070/pexels-photo-934070.jpeg",
        "https://images.pexels.com/photos/532220/pexels-photo-532220.jpeg",
        "https://images.pexels.com/photos/2988634/pexels-photo-2988634.jpeg",
        "https://images.pexels.com/photos/428340/pexels-photo-428340.jpeg",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
    ],
    "Watches": [
        "https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg",
        "https://images.unsplash.com/photo-1464983953574-0892a716854b",
        "https://images.unsplash.com/photo-1513648077-8bfa3ec94421",
        "https://images.pexels.com/photos/19090/pexels-photo.jpg",
        "https://images.pexels.com/photos/428343/pexels-photo-428343.jpeg",
        "https://images.unsplash.com/photo-1503342452485-86a096e77d79",
        "https://images.unsplash.com/photo-1519750157634-bbb07f2d7c92",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        "https://images.pexels.com/photos/428363/pexels-photo-428363.jpeg",
        "https://images.pexels.com/photos/2983463/pexels-photo-2983463.jpeg",
    ],
    "Ties": [
        "https://images.pexels.com/photos/2983447/pexels-photo-2983447.jpeg",
        "https://images.pexels.com/photos/428344/pexels-photo-428344.jpeg",
        "https://images.unsplash.com/photo-1519750157634-bbb07f2d7c92",
        "https://images.pexels.com/photos/935958/pexels-photo-935958.jpeg",
        "https://images.pexels.com/photos/2553655/pexels-photo-2553655.jpeg",
        "https://images.pexels.com/photos/882070/pexels-photo-882070.jpeg",
        "https://images.pexels.com/photos/428340/pexels-photo-428340.jpeg",
        "https://images.pexels.com/photos/428342/pexels-photo-428342.jpeg",
        "https://images.pexels.com/photos/428341/pexels-photo-428341.jpeg",
        "https://images.pexels.com/photos/934091/pexels-photo-934091.jpeg",
    ],
    "Sunglasses": [
        "https://images.pexels.com/photos/46710/pexels-photo-46710.jpeg",
        "https://images.unsplash.com/photo-1513648077-8bfa3ec94421",
        "https://images.pexels.com/photos/428343/pexels-photo-428343.jpeg",
        "https://images.unsplash.com/photo-1529333166437-7750a6dd5a70",
        "https://images.pexels.com/photos/428344/pexels-photo-428344.jpeg",
        "https://images.pexels.com/photos/358574/pexels-photo-358574.jpeg",
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        "https://images.unsplash.com/photo-1464983953574-0892a716854b",
        "https://images.pexels.com/photos/934070/pexels-photo-934070.jpeg",
        "https://images.pexels.com/photos/936077/pexels-photo-936077.jpeg",
    ],
    "Hats": [
        "https://images.pexels.com/photos/936099/pexels-photo-936099.jpeg",
        "https://images.unsplash.com/photo-1519750157634-bbb07f2d7c92",
        "https://images.unsplash.com/photo-1513648077-8bfa3ec94421",
        "https://images.unsplash.com/photo-1465188162913-8a1049b2a8ff",
        "https://images.pexels.com/photos/934070/pexels-photo-934070.jpeg",
        "https://images.pexels.com/photos/428343/pexels-photo-428343.jpeg",
        "https://images.pexels.com/photos/358574/pexels-photo-358574.jpeg",
        "https://images.pexels.com/photos/247917/pexels-photo-247917.jpeg",
        "https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg",
        "https://images.pexels.com/photos/2988637/pexels-photo-2988637.jpeg",
    ],
}

DETAILS = {
    "Shirts": [
        "100% premium cotton. Regular fit, perfect for work or weekend.",
        "Slim-fit linen shirt with a classic collar and button fastening.",
        "White formal shirt, wrinkle-resistant fabric.",
        "Checked casual shirt for outings and Friday wear.",
        "Light-blue full-sleeve shirt, moisture-wicking.",
        "Floral print shirt for beach vacations.",
        "Striped business shirt, easy-iron finish.",
        "Short sleeve pastel shirt for warm days.",
        "Dark navy oxford shirt, modern elegance.",
        "Black solid slim-fit shirt for evenings.",
    ],
    "Trousers": [
        "Classic navy formal trousers for office.",
        "Chino trousers in sand color, versatile wear.",
        "Slim-fit black trousers with stretch waist.",
        "Grey checkered trousers, soft wool blend.",
        "Beige cotton casual trousers, comfortable all day.",
        "Relaxed fit joggers in athletic knit.",
        "Olive green cargo trousers, multiple pockets.",
        "Denim blue jeans, regular fit.",
        "Textured formal trousers, premium finish.",
        "Slim brown trousers with easy-care fabric.",
    ],
    "Jackets": [
        "Black leather biker jacket, fully lined.",
        "Smart blue blazer for business meetings.",
        "Waterproof windcheater, lightweight.",
        "Denim trucker jacket, stone washed.",
        "Puffer jacket, thermal insulation for winters.",
        "Bomber jacket with ribbed cuffs.",
        "Camel colored trench coat, classic style.",
        "Reversible sports jacket.",
        "Formal evening jacket, peak lapel.",
        "Olive quilted jacket, weather-resistant.",
    ],
    "Shoes": [
        "Brown leather Derby shoes, comfort insole.",
        "White canvas casual sneakers.",
        "Formal black Oxford lace-up shoes.",
        "Tan suede loafers, slip-on style.",
        "High-top running sneakers with mesh upper.",
        "Blue boat shoes with contrast laces.",
        "Grey slip-on trainers, ultralight.",
        "Monk strap formal shoes, dual buckle.",
        "Ankle-length Chelsea boots, black.",
        "Espadrille woven shoes, holiday style.",
    ],
    "Belts": [
        "Elegant black leather with brushed buckle.",
        "Brown reversible belt, classic square buckle.",
        "Stretchable woven fabric belt for casual wear.",
        "Automatic buckle tan leather belt.",
        "Wide formal belt with chrome detailing.",
        "Canvas webbing belt, adjustable.",
        "Premium designer leather belt.",
        "Synthetic slim-fit dress belt.",
        "Nylon track belt for adventure.",
        "Vintage-inspired braided belt.",
    ],
    "Wallets": [
        "Bi-fold leather wallet, RFID protected.",
        "Minimalist cardholder with money clip.",
        "Tan slim wallet with coin pocket.",
        "Classic black wallet, 6 card slots.",
        "Designer wallet, contrast stitching.",
        "Travel wallet with zipper compartment.",
        "Textured brown compact wallet.",
        "Canvas wallet, machine washable.",
        "Elegant vegan leather wallet.",
        "Vintage money purse with snap.",
    ],
    "Watches": [
        "Analog black dial stainless steel band.",
        "Digital sports watch, water resistant.",
        "Brown leather chronograph watch.",
        "Blue dial quartz watch, classic style.",
        "Smartwatch with heart rate tracker.",
        "Square face retro digital watch.",
        "Dress watch, minimalist silver casing.",
        "Diver's wristwatch, glow-in-dark hands.",
        "Mesh band automatic mechanical watch.",
        "Vintage pocket watch, chain included.",
    ],
    "Ties": [
        "Navy silk tie with microdot pattern.",
        "Classic red striped tie.",
        "Slim black tie, formal evenings.",
        "Paisley print tie, vibrant accents.",
        "Light green cotton-linen blend tie.",
        "Diagonal silver stripe tie.",
        "Textured knit navy tie.",
        "Royal blue tie with subtle sheen.",
        "Burnt orange geometric pattern tie.",
        "Burgundy woven formal tie.",
    ],
    "Sunglasses": [
        "Classic aviator, UV protection.",
        "Wayfarer sunglasses, scratch-resistant.",
        "Round retro frame sunglasses.",
        "Polarized wraparound sports shades.",
        "Mirrored lens, fashion forward.",
        "Transparent frame, modern vibe.",
        "Square frame, anti-glare coating.",
        "Clip-on convertible style.",
        "Matte black oversized shades.",
        "Tortoiseshell formal sunglasses.",
    ],
    "Hats": [
        "Classic trilby hat, wool blend.",
        "Baseball cap, breathable mesh panels.",
        "Wide brim straw hat for sun.",
        "Black beanie for winter warmth.",
        "Golf visor, moisture-wicking band.",
        "Grey snapback, flat brim.",
        "Newsboy cap, vintage tailoring.",
        "Fedora hat, ribbon detail.",
        "Padded bucket hat for rainy days.",
        "Checkered driver cap, casual chic.",
    ],
}

PRICES = {
    "Shirts": [899, 1199, 1399, 999, 1299, 1599, 1099, 899, 1499, 1349],
    "Trousers": [1299, 1399, 1399, 1699, 1249, 1199, 1349, 1450, 1750, 1599],
    "Jackets": [2999, 4999, 1599, 2399, 3199, 2199, 3899, 2390, 2850, 3220],
    "Shoes": [1799, 2250, 2100, 2499, 3299, 1999, 1650, 2349, 2799, 1200],
    "Belts": [799, 950, 650, 1200, 1580, 700, 2400, 659, 989, 1100],
    "Wallets": [999, 699, 849, 1099, 1899, 799, 500, 899, 999, 499],
    "Watches": [1999, 2300, 3499, 1750, 3999, 1599, 2500, 3750, 5200, 1450],
    "Ties": [650, 499, 399, 899, 799, 499, 750, 599, 929, 699],
    "Sunglasses": [1349, 1490, 1960, 2150, 1050, 1875, 2180, 1300, 1525, 1635],
    "Hats": [499, 399, 899, 599, 799, 549, 885, 1190, 650, 750],
}

SIZING = {
    "Shirts": "S,M,L,XL",
    "Trousers": "30,32,34,36,38",
    "Jackets": "M,L,XL,XXL",
    "Shoes": "UK7,UK8,UK9,UK10,UK11",
    "Belts": "32,34,36,38,40",
    "Wallets": "",   # Not sized
    "Watches": "",   # Not sized
    "Ties": "",      # Not sized
    "Sunglasses": "",  # Not sized
    "Hats": "M,L,XL",
}

# -- Prepare products for bulk insert/update --
PRODUCTS = []
for cat in CATEGORIES:
    catname = cat["name"]
    for i in range(10):
        PRODUCTS.append({
            "name": f"{catname[:-1] if catname.endswith('s') else catname} {i + 1}",
            "description": DETAILS[catname][i],
            "image_url": IMAGES[catname][i],
            "price": PRICES[catname][i],
            "available_sizes": SIZING.get(catname, ""),
            "category_name": catname,
        })

# PUBLIC_INTERFACE
def seed_categories_and_products(db: Session):
    """
    PUBLIC_INTERFACE: Seeds only men's apparel and accessories categories/products.
    Wipes sports/outdated categories, always produces 10 products per category with initial data.
    """
    allowed_names = set([c["name"] for c in CATEGORIES])

    # Remove products not in allowed categories
    for prod in db.query(models.Product).all():
        cat = db.query(models.ProductCategory).filter_by(id=prod.category_id).first()
        if cat is None or cat.name not in allowed_names:
            db.delete(prod)
    db.commit()

    # Remove all categories not in whitelist
    for cat in db.query(models.ProductCategory).all():
        if cat.name not in allowed_names:
            db.delete(cat)
    db.commit()

    # Insert/update categories
    name_to_cat = {}
    for c in CATEGORIES:
        category = db.query(models.ProductCategory).filter_by(name=c["name"]).first()
        if not category:
            category = models.ProductCategory(name=c["name"], description=c["description"])
            db.add(category)
            db.commit()
        name_to_cat[c["name"]] = category
    db.commit()

    # Insert/update 10 products per category
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
