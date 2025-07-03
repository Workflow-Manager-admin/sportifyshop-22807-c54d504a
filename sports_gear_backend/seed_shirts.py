import sys
import os

if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src", "api")))
    from src.api import seed_data
    print("Seeding 10 shirt products...")
    seed_data.seed_shirt_products()
    print("Done.")
