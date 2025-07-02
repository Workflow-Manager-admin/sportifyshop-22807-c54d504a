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

1. Install dependencies (`pip install -r requirements.txt`)
2. Run the server: `uvicorn src.api.main:app --reload`
3. API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
