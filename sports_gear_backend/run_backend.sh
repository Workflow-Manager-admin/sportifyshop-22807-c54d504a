#!/bin/bash
# Launch the FastAPI server on 0.0.0.0:8000 for development, Docker, VM, or Codespaces.
# Usage: bash run_backend.sh
cd "$(dirname "$0")" || exit 1

echo "Launching backend at http://0.0.0.0:8000 (accessible from Docker, VM, or cloud IDE)..."
uvicorn main:app --reload --host 0.0.0.0 --port 8000
