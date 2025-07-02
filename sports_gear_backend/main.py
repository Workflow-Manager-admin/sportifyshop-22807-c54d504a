"""
FastAPI/uvicorn entrypoint to enable correct src package import from backend root.
Run with: uvicorn main:app --reload --host 0.0.0.0 --port 8000

Ensures src is on sys.path so src.api.main:app can be imported cleanly.
"""

import sys
import os
import logging

# Patch sys.path so that 'src' is importable regardless of working directory
_BACKEND_ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_ABSPATH = os.path.abspath(os.path.join(_BACKEND_ROOT, "src"))
if SRC_ABSPATH not in sys.path:
    sys.path.insert(0, SRC_ABSPATH)

try:
    from api.main import app
except ImportError as e:
    # Helpful error log for import issues
    raise ImportError(
        f"Failed to import app. sys.path: {sys.path}\n"
        f"Tried to import from: {SRC_ABSPATH}/api/main.py\n"
        f"Error: {e}"
    )

__all__ = ["app"]

# Optionally add logging to help debug startup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastapi")
logger.info("sports_gear_backend.main.py loaded. FastAPI app should be ready.")
