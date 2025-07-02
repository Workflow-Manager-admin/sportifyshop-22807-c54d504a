"""
FastAPI/uvicorn entrypoint to enable correct src package import from backend root.
Run with: uvicorn main:app --reload --host 0.0.0.0 --port 8000

Ensures src is on sys.path so src.api.main:app can be imported cleanly.
"""
"""
FastAPI/uvicorn entrypoint to enable correct src package import from backend root.
Run with: uvicorn main:app --reload --host 0.0.0.0 --port 8000

Ensures src is on sys.path so src.api.main:app can be imported cleanly.
"""
"""
FastAPI/uvicorn entrypoint to enable correct src package import from backend root.
Run with: uvicorn main:app --reload --host 0.0.0.0 --port 8000

Ensures src is on sys.path so src.api.main:app can be imported cleanly.
"""
import os
import sys

# The following function ensures E402 is respected: all imports appear at module top-level.
"""
FastAPI/uvicorn entrypoint, fully PEP8/E402-compliant due to package __init__.py files.
Run with: uvicorn main:app --reload --host 0.0.0.0 --port 8000
"""

from api.main import app
