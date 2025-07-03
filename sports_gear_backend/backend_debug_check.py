"""
Script: backend_debug_check.py
Purpose: 
- Directly check if 'admin@example.com' exists in the SQLite users table.
- Print the bcrypt hash and full user row.
- Test and print if password 'admin123' verifies with the stored hash using backend hashing logic.
Usage:
  python backend_debug_check.py

This script should be run from the sports_gear_backend folder or adjust path accordingly.
"""

from sqlalchemy.orm import sessionmaker
from src.api.models import User, get_engine
from src.api.main import verify_password, get_password_hash

def debug_admin_user():
    engine = get_engine(echo=False)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    admin_email = "admin@example.com"

    user = db.query(User).filter_by(email=admin_email).first()
    if user:
        print("User found: admin@example.com")
        print("Full DB row:", dict(
            id=user.id, email=user.email, hashed_password=user.hashed_password, full_name=user.full_name, is_active=user.is_active
        ))
        # Check password
        plain_pw = "admin123"
        checked = verify_password(plain_pw, user.hashed_password)
        print(f"Password check for 'admin123': {'SUCCESS' if checked else 'FAIL'}")

        # Manual check: show what the hash of admin123 (fresh) looks like
        manual_hash = get_password_hash(plain_pw)
        print("Freshly generated hash for 'admin123':", manual_hash)
        # Also check using backend function
        print("Does verify_password() accept freshly generated hash?", verify_password(plain_pw, manual_hash))
    else:
        print("admin@example.com not found in users table.")

    db.close()

if __name__ == "__main__":
    debug_admin_user()
