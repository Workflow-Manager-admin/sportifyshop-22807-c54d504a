# sportifyshop-22807-c54d504a

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
2. Run the server:
   - From inside `sports_gear_backend` folder:  
     ```
     uvicorn src.api.main:app --reload
     ```
     OR (if you want to ensure `src` always imports cleanly regardless of CWD):
     ```
     uvicorn main:app --reload
     ```
     This uses `main.py` which sets up Python path for `src` imports.

   - **From project root**  
     If running from project root (`sportifyshop-22807-c54d504a/`), you can:
     ```
     cd sports_gear_backend
     uvicorn main:app --reload
     ```
     Trying to run directly from project root with a command like
     ```
     uvicorn sports_gear_backend.src.api.main:app --reload
     ```
     is **not supported** unless the Python path is configured explicitly.

3. API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

#### Common error: "No module named 'src'"
- This occurs if you run `uvicorn` from a directory where the `src` module is not on `PYTHONPATH`.
- Always run uvicorn from within `sports_gear_backend` using `main:app`, or set your PYTHONPATH accordingly.
- If you see this error, double-check your working directory and use the above instructions.

