"""
Seed script for restricted sports gear categories and products:
Seeds only the following product types: balls, Apparel, shoes, socks, bat, hockey bat, baseball bat.
Each type has exactly 10 unique products with default price, valid public image URL, and consistent size where appropriate.
Removes all other categories and products from the seeding logic.
"""

from sqlalchemy.orm import Session
from . import models

# --- STATIC CATEGORIES ---
CATEGORIES = [
    {"name": "Balls", "description": "Sports balls including cricket, football, tennis, and more"},
    {"name": "Apparel", "description": "Sports clothing including jerseys, shorts, tracksuits"},
    {"name": "Shoes", "description": "Running shoes and athletic footwear"},
    {"name": "Socks", "description": "Sports socks for comfort and performance"},
    {"name": "Bat", "description": "Cricket bats for all levels"},
    {"name": "Hockey Bat", "description": "High-quality hockey bats"},
    {"name": "Baseball Bat", "description": "Durable baseball bats for all ages"},
]

# --- PRODUCT URLS ---
BALL_IMAGES = [
    "https://images.unsplash.com/photo-1517649763962-0c623066013b?auto=format&fit=crop&w=500&q=80",  # Cricket ball
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=500&q=80",  # Football
    "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=500&q=80",  # Basketball
    "https://images.unsplash.com/photo-1519864600265-abb23847ef2c?auto=format&fit=crop&w=500&q=80",  # Tennis ball
    "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=500&q=80",  # Volleyball
    "https://images.unsplash.com/photo-1508873699372-7aeab60b44c9?auto=format&fit=crop&w=500&q=80",  # Rugby ball
    "https://images.unsplash.com/photo-1448894977689-142b4048a28c?auto=format&fit=crop&w=500&q=80",  # Baseball
    "https://images.unsplash.com/photo-1515524738708-327f6b0037a7?auto=format&fit=crop&w=500&q=80",  # Softball
    "https://images.unsplash.com/photo-1516728778615-2d590ea185ee?auto=format&fit=crop&w=500&q=80",  # Handball
    "https://images.unsplash.com/photo-1514511634509-579097eber14?auto=format&fit=crop&w=500&q=80",  # Hockey ball
]
APPAREL_IMAGES = [
    "https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=600&q=80",  # Jersey
    "https://images.unsplash.com/photo-1526178613658-3c73fcf1805c?auto=format&fit=crop&w=600&q=80",  # Shorts
    "https://images.unsplash.com/photo-1515984979728-cb7b4a2d1d1c?auto=format&fit=crop&w=600&q=80",  # Hoodie
    "https://images.unsplash.com/photo-1519710164239-da123dc03ef4?auto=format&fit=crop&w=600&q=80",  # Tracksuit
    "https://images.unsplash.com/photo-1531259683007-016a7b628fc3?auto=format&fit=crop&w=600&q=80",  # Tank top
    "https://images.unsplash.com/photo-1530847887473-93c3d1a1eb0d?auto=format&fit=crop&w=600&q=80",  # Training tee
    "https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?auto=format&fit=crop&w=600&q=80",  # Sleeveless
    "https://images.unsplash.com/photo-1526271083670-92ee58c7c51d?auto=format&fit=crop&w=600&q=80",  # Compression shirt
    "https://images.unsplash.com/photo-1465188162913-8a1049b2a8ff?auto=format&fit=crop&w=600&q=80",  # Sport bra
    "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=600&q=80",  # Training pants
]
SHOES_IMAGES = [
    "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1517263904808-5dc0d07fe126?auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1465101178521-c1a9136a1803?auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1456327102063-fb5054efe647?auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1468476396571-cfc36d83f2b1?auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1504215680853-026ed2a45def?auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1470246973918-29a93221c455?auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1519864600265-abb23847ef2c?auto=format&fit=crop&w=600&q=80",
    "https://images.unsplash.com/photo-1508614969033-2473d392e2c5?auto=format&fit=crop&w=600&q=80",
]
SOCKS_IMAGES = [
    "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=500&q=80",  # White
    "https://images.unsplash.com/photo-1519864600265-abb23847ef2c?auto=format&fit=crop&w=500&q=80",  # Black
    "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=500&q=80",  # Red
    "https://images.unsplash.com/photo-1468476396571-cfc36d83f2b1?auto=format&fit=crop&w=500&q=80",  # Blue
    "https://images.unsplash.com/photo-1456327102063-fb5054efe647?auto=format&fit=crop&w=500&q=80",  # Sport
    "https://images.unsplash.com/photo-1516715094483-1c9b7c3c4d19?auto=format&fit=crop&w=500&q=80",  # Running
    "https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?auto=format&fit=crop&w=500&q=80",  # Nylon
    "https://images.unsplash.com/photo-1514432324607-a09d9c10a43c?auto=format&fit=crop&w=500&q=80",  # Ankle
    "https://images.unsplash.com/photo-1513267048332-d994b6d7f6ce?auto=format&fit=crop&w=500&q=80",  # Cushion
    "https://images.unsplash.com/photo-1506501139099-cb7466e021b7?auto=format&fit=crop&w=500&q=80",  # Crew
]
BAT_IMAGES = [
    "https://cdn.pixabay.com/photo/2016/12/27/16/33/cricket-1937286_960_720.jpg",
    "https://5.imimg.com/data5/SELLER/Default/2020/8/IW/MB/YG/24166495/english-willow-cricket-bat-500x500.jpg",
    "https://images.unsplash.com/photo-1516747773441-f858a1e9b441?auto=format&fit=crop&w=500&q=80",
    "https://m.media-amazon.com/images/I/41r0HeoPRTL.jpg",
    "https://cdn.shopify.com/s/files/1/0551/9246/9116/products/SGR17INFA020-BAT_800x.jpg?v=1628745408",
    "https://www.pngitem.com/pimgs/m/288-2884690_cricket-bat-png-transparent-png.png",
    "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=500&q=80",
    "https://static-01.daraz.pk/p/0e57ffed37e27eab57d0e892bdecf8d8.jpg",
    "https://image.shutterstock.com/image-photo/cricket-bat-isolated-on-white-260nw-1366933274.jpg",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=500&q=80"
]
HOCKEY_BAT_IMAGES = [
    "https://m.media-amazon.com/images/I/61rOHAyYtWL._SL1500_.jpg",
    "https://n1.sdlcdn.com/imgs/a/2/b/Hockey-Bat-SDL173961455-1-4f7e2.jpg",
    "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=600&q=80",
    "https://qph.cf2.quoracdn.net/main-qimg-dcb2ef715b7a9921629cbd228e251fae-lq",
    "https://m.media-amazon.com/images/I/61R7GZ0v4aL._SX342_.jpg",
    "https://cdn11.bigcommerce.com/s-47p22kzvda/images/stencil/1280x1280/products/464/1809/JK-Hockey-Bat-Red__23288.1626343397.jpg?c=2",
    "https://images.unsplash.com/photo-1519864600265-abb23847ef2c?auto=format&fit=crop&w=600&q=80",
    "https://rukminim2.flixcart.com/image/416/416/kh80v0w0/hockey-stick/i/t/l/36-5-hockey-stick-wish-original-imafx3czpajthj6j.jpeg?q=70",
    "https://www.khelmart.com/blogs/wp-content/uploads/2021/04/Top-8-Hockey-Bat-1.jpg",
    "https://images.unsplash.com/photo-1506501139099-cb7466e021b7?auto=format&fit=crop&w=500&q=80",
]
BASEBALL_BAT_IMAGES = [
    "https://images.unsplash.com/photo-1448894977689-142b4048a28c?auto=format&fit=crop&w=600&q=80",
    "https://static.toiimg.com/thumb/msid-72769541,width-1280,resizemode-4/72769541.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Baseball-bat.jpg/800px-Baseball-bat.jpg",
    "https://5.imimg.com/data5/TG/QF/MY-2207665/wooden-baseball-bat-500x500.jpg",
    "https://www.hamillbaseball.com/library/images/SSK-BLUE.png",
    "https://images.unsplash.com/photo-1508614969033-2473d392e2c5?auto=format&fit=crop&w=600&q=80",
    "https://m.media-amazon.com/images/I/41n1yeYx5kL.jpg",
    "https://www.anniegarland.com/wp-content/uploads/2020/11/baseball-bat.jpg",
    "https://dksports.com/cdn/shop/products/WOODEN_BASEBALL_BAT.jpg?v=1634761875",
    "https://target.scene7.com/is/image/Target/GUEST_680ca026-d25e-4d83-8c67-e74044e3de85?wid=488&hei=488&fmt=pjpeg",
]

# --- DEFAULT VALUES ---
CATEGORY_INFO = {
    "Balls": {
        "type_prefix": "Sports Ball",
        "default_price": 20.0,
        "default_sizes": "4,5",
        "images": BALL_IMAGES,
    },
    "Apparel": {
        "type_prefix": "Jersey",
        "default_price": 30.0,
        "default_sizes": "S,M,L,XL",
        "images": APPAREL_IMAGES,
    },
    "Shoes": {
        "type_prefix": "Running Shoe",
        "default_price": 40.0,
        "default_sizes": "UK7,UK8,UK9,UK10",
        "images": SHOES_IMAGES,
    },
    "Socks": {
        "type_prefix": "Sports Sock",
        "default_price": 8.0,
        "default_sizes": "M,L,XL",
        "images": SOCKS_IMAGES,
    },
    "Bat": {
        "type_prefix": "Cricket Bat",
        "default_price": 60.0,
        "default_sizes": "Standard",
        "images": BAT_IMAGES,
    },
    "Hockey Bat": {
        "type_prefix": "Hockey Bat",
        "default_price": 55.0,
        "default_sizes": "Standard",
        "images": HOCKEY_BAT_IMAGES,
    },
    "Baseball Bat": {
        "type_prefix": "Baseball Bat",
        "default_price": 50.0,
        "default_sizes": "Standard",
        "images": BASEBALL_BAT_IMAGES,
    },
}

# --- PRODUCT PREP ---
PRODUCTS = []
for cat in CATEGORIES:
    catname = cat["name"]
    info = CATEGORY_INFO[catname]
    for i in range(1, 11):
        PRODUCTS.append({
            "name": f"{info['type_prefix']} {i}",
            "description": f"{info['type_prefix']} model no. {i}",
            "image_url": info["images"][(i - 1) % len(info["images"])],
            "price": info["default_price"],
            "available_sizes": info["default_sizes"],
            "category_name": catname,
        })

# PUBLIC_INTERFACE
def seed_categories_and_products(db: Session):
    """
    PUBLIC_INTERFACE: Seed only categories and products for balls, Apparel, shoes, socks, bat, hockey bat, baseball bat.
    All other categories/products removed. Always creates 10 products per type, unique names, with default price, sizes, and public images.
    """
    # Delete any products/categories not in our whitelist to ensure idempotency
    allowed_cat_names = set([c["name"] for c in CATEGORIES])
    # Remove ALL products not in allowed categories
    for prod in db.query(models.Product).all():
        cat = db.query(models.ProductCategory).filter_by(id=prod.category_id).first()
        if cat is None or cat.name not in allowed_cat_names:
            db.delete(prod)
    db.commit()
    # Remove all categories not in allowed list
    for cat in db.query(models.ProductCategory).all():
        if cat.name not in allowed_cat_names:
            db.delete(cat)
    db.commit()
    # Insert/update allowed categories
    name_to_cat = {}
    for c in CATEGORIES:
        category = db.query(models.ProductCategory).filter_by(name=c["name"]).first()
        if not category:
            category = models.ProductCategory(name=c["name"], description=c["description"])
            db.add(category)
            db.commit()
        name_to_cat[c["name"]] = category
    db.commit()
    # Insert/update 10 products for each category
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
