import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sports_gear_backend.src.models import Product, UploadedImage
from dotenv import load_dotenv

"""
Script to purge all products, product-category relationships, and uploaded images from the database and filesystem.
After running this, the catalog and image folders will be empty/clean.
"""

# Load .env configuration for DB connection etc
load_dotenv()

DB_URL = os.getenv("DATABASE_URL", None)
SQLITE_PATH = os.path.join(os.path.dirname(__file__), "../sports_gear.db")
IMAGE_UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploaded_images")

def remove_all_images_from_folder(upload_folder):
    if os.path.isdir(upload_folder):
        for filename in os.listdir(upload_folder):
            file_path = os.path.join(upload_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted {file_path}")

def main():
    if DB_URL:
        engine = sqlalchemy.create_engine(DB_URL, connect_args={"check_same_thread": False})
    else:
        engine = sqlalchemy.create_engine(f"sqlite:///{SQLITE_PATH}", connect_args={"check_same_thread": False})

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    # Delete all data from Product, UploadedImage, Product-Category relationship
    try:
        # For SQLAlchemy - assuming UploadedImage is used, otherwise skip
        if UploadedImage in Base._decl_class_registry.values():
            session.query(UploadedImage).delete()
        session.query(Product).delete()
        # If there is a relationship/join table, remove it as well (usually ProductCategory, but adjust as needed)
        if 'product_category' in Base.metadata.tables:
            session.execute('DELETE FROM product_category')
        session.commit()
        print("Deleted all products and images from the database.")
    except Exception as e:
        session.rollback()
        print(f"Failed to clear database: {e}")
    finally:
        session.close()

    # Remove uploaded images manually from folder
    remove_all_images_from_folder(IMAGE_UPLOAD_FOLDER)
    print("Purge completed.")

if __name__ == "__main__":
    # ORM Base setup
    try:
        from sports_gear_backend.src.models import Base
    except ImportError:
        print("Error: Could not import ORM Base from models. Please check the models.py for Base declaration.")
        exit(1)
    main()
