"""
Script to purge all products and associated images from the local database and storage.

Run this script directly to delete ALL current product data and images.
"""

import os
import sqlite3

# Database and images directory configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "sports_gear.db")
IMAGES_DIR = os.path.join(BASE_DIR, "uploaded_images")

def delete_all_products():
    """
    Delete all products from the products table in the database.
    """
    if not os.path.exists(DB_PATH):
        print(f"No database found at {DB_PATH}. Nothing to do.")
        return

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Get image filenames before deletion (if the table exists)
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products';")
        if not cursor.fetchone():
            print("No products table found. Skipping database product purge.")
        else:
            try:
                cursor.execute("SELECT image_url FROM products;")
                # Fetch image URLs (previously: image_urls = ...)
                cursor.fetchall()  # Just fetch without assignment to avoid unused var
            except Exception:
                pass  # Ignore if select fails

            cursor.execute("DELETE FROM products;")
            conn.commit()
            print("All products have been deleted from the database.")

        conn.close()
    except Exception as e:
        print(f"Failed to delete products: {e}")

def delete_all_images():
    """
    Delete all image files from the uploaded_images directory.
    """
    if not os.path.exists(IMAGES_DIR):
        print(f"No images directory found at {IMAGES_DIR}. Nothing to do.")
        return

    image_files = os.listdir(IMAGES_DIR)
    removed_count = 0
    for filename in image_files:
        filepath = os.path.join(IMAGES_DIR, filename)
        try:
            if os.path.isfile(filepath):
                os.remove(filepath)
                removed_count += 1
        except Exception as e:
            print(f"Could not delete {filepath}: {e}")
    print(f"Deleted {removed_count} images from {IMAGES_DIR}.")

def purge():
    """
    PUBLIC_INTERFACE
    Purge all product entries and images from the backend.
    """
    print("Purging all products from the database...")
    delete_all_products()
    print("Purging all images from storage...")
    delete_all_images()
    print("Purge completed successfully.")

if __name__ == "__main__":
    purge()
