# sportifyshop-22807-c54d504a

---
🚩 **IMPORTANT: For Docker, VM, Codespaces, or Cloud IDEs, ALWAYS use `--host 0.0.0.0` when running the backend, or use the provided `run_backend.sh` script!**
- If you only use `127.0.0.1` (the default), the server will not be accessible from outside the container/VM/cloud, and the frontend or your browser may NOT be able to connect.
---

## Backend Setup – `sports_gear_backend`

This backend is built with FastAPI and uses SQLite via SQLAlchemy ORM. It provides the data models and server structure for the Sports Gear ecommerce shop.

### Features

- **User management**: Registration, login, profile management
- **Product catalog**: Browsing, search, detail pages, real-time prices and categories
- **Shopping cart**: Add to cart, update, remove, manage cart
- **Order management**: Checkout, Stripe payment integration, order history
- **Database health check**: `/db/health` endpoint

### Data Models

- **User**
- **ProductCategory**
- **Product**
- **Cart**
- **CartItem**
- **Order**
- **OrderItem**

### Structure

- `src/api/main.py`: FastAPI application with core endpoints and DB health
- `src/api/models.py`: Database models, ORM config, DB init routines

### Database

Uses SQLite DB (`sports_gear.db` by default, override with `SQLITE_DB_FILENAME` env var).

### Running and developing

#### Recommended: Run backend from the sports_gear_backend folder

1. Install dependencies (`pip install -r requirements.txt`)
2. Run the server (**highly recommended**):  
   - From inside `sports_gear_backend` folder:
     ```
     bash run_backend.sh
     ```
     *(This script runs uvicorn with `--host 0.0.0.0` for maximum compatibility)*

   - OR manually:
     ```
     uvicorn src.api.main:app --reload --host 0.0.0.0
     ```
     OR (to ensure `src` always imports cleanly regardless of CWD):
     ```
     uvicorn main:app --reload --host 0.0.0.0
     ```
     This uses `main.py` which sets up Python path for `src` imports.

   - **From project root**  
     If running from project root (`sportifyshop-22807-c54d504a/`), you should:
     ```
     cd sports_gear_backend
     bash run_backend.sh
     ```
     (Or use `uvicorn main:app --reload --host 0.0.0.0`)

     Trying to run directly from project root with a command like
     ```
     uvicorn sports_gear_backend.src.api.main:app --reload
     ```
     is **not supported** unless the Python path is configured explicitly.

3. API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

#### 🚩 Trouble accessing on http://127.0.0.1:8000/docs but backend says "running"?
If you start uvicorn and see "Application startup complete" but the docs page is unreachable:

- **Check port and host binding:** By default, `uvicorn` binds to 127.0.0.1 (localhost). If you're in a container, Docker, VM, or cloud IDE, use:
  ```
  uvicorn main:app --reload --host 0.0.0.0
  ```
  (Or add `--host 0.0.0.0` to any uvicorn command.)  
  This lets all network interfaces access the API (required for remote/browser access in Docker/cloud).

- **If running inside Docker or a remote dev environment or codespace:**  
  Access via the exposed/public URL, not "localhost", unless port forwarding is set up.

- **Port conflicts:** Make sure port 8000 isn't used by another app. Change with `--port 8001` etc, if needed.

- **Firewall/security group:** Ensure inbound connections to port 8000 are allowed (rarely needed for local-only).

- **Wrong working directory:** Always `cd sports_gear_backend` before starting uvicorn `main:app`.

- **Check that FastAPI started successfully:** If uvicorn crashes or logs import errors, confirm Python path and dependencies.

- **In cloud/dev containers:**  
  Your backend is usually available on an external/public URL shown by your dev environment (not http://127.0.0.1:8000). For example, see your codespace or cloud IDE's port-forwarded address.

**For local development (all OS):**
```
uvicorn main:app --reload --host 0.0.0.0
```
- Visit http://localhost:8000/docs or use the forwarded/public address from your environment.

---

#### Common error: "No module named 'src'"
- This occurs if you run `uvicorn` from a directory where the `src` module is not on `PYTHONPATH`.
- Always run uvicorn from within `sports_gear_backend` using `main:app`, or set your PYTHONPATH accordingly.
- If you see this error, double-check your working directory and use the above instructions.

