import os
import sys
from src.api import seed_data
from src.api.models import get_session_local

# Ensure sys.path is correctly set for local imports if called as script
sys.path.append(os.path.join(os.path.dirname(__file__), "src", "api"))

if __name__ == "__main__":
    SessionLocal = get_session_local()
    db = SessionLocal()
    seed_data.seed_categories_and_products(db)
