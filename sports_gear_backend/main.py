"""
FastAPI/uvicorn entrypoint to enable correct src package import from backend root.
Run with: uvicorn main:app --reload --host 0.0.0.0 --port 8000

Ensures src is on sys.path so src.api.main:app can be imported cleanly.
"""

import logging
from api.main import app

__all__ = ["app"]

# Optionally add logging to help debug startup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastapi")
logger.info("sports_gear_backend.main.py loaded. FastAPI app should be ready.")
