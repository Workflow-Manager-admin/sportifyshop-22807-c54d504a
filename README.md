# manstyle-hub-backend

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

#### 🚩 Trouble accessing from another device? (e.g. http://192.168.70.40:8000/docs or LAN IP)

If you start uvicorn (or run_backend.sh) and see "Application startup complete" but the docs page is unreachable from other devices on your LAN:

**Advanced network diagnostics:**  
1. Make sure you are running with `--host 0.0.0.0` (see above).
2. Run the built-in debug scripts:
   - For backend service health:  
     ```
     python backend_debug_check.py
     ```
   - For network troubleshooting & firewall:
     ```
     bash network_debug_check.sh
     ```
     This will print info about which interface(s) are listening, if the firewall/iptables is blocking, process usage, and LAN interface status.
3. **If port 8000 is NOT listening on 0.0.0.0 OR not accessible:**
   - Check if your OS firewall is blocking access (see the output for iptables/ufw status).
   - Temporarily disable firewall for a test (Linux):  
     ```
     sudo ufw disable
     ```
     or open only that port:
     ```
     sudo ufw allow 8000/tcp
     ```
   - For firewalld:
     ```
     sudo firewall-cmd --add-port=8000/tcp --permanent && sudo firewall-cmd --reload
     ```
   - If you are in Docker or a VM, ensure proper port mapping/forwarding (`docker run -p 8000:8000 ...` or similar).
   - Check your PC's network configuration (are you on a VPN? On the correct interface?).
   - Try accessing `curl http://127.0.0.1:8000` and `curl http://0.0.0.0:8000` on the backend machine itself, and also from another device (use your machine's LAN IP such as `http://192.168.70.40:8000`).
4. If unable to solve, copy the full output of both debug scripts to your support request – include any error or port conflicts reported.

---

**For local development (all OS):**
```
uvicorn main:app --reload --host 0.0.0.0
```
- Visit http://localhost:8000/docs from the *same machine*.
- Visit http://<YOUR_LOCAL_IP>:8000/docs (e.g., http://192.168.70.40:8000/docs) from another device *on your LAN*, after confirming firewall/network access.

---

#### Common error: "No module named 'src'"
- This occurs if you run `uvicorn` from a directory where the `src` module is not on `PYTHONPATH`.
- Always run uvicorn from within `sports_gear_backend` using `main:app`, or set your PYTHONPATH accordingly.
- If you see this error, double-check your working directory and use the above instructions.

