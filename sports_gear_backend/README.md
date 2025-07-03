# Backend Deployment & Nginx Setup Notes

> This document provides information relevant to backend deployment and any web/reverse proxy server (e.g. nginx) problems.

## Nginx 404 Troubleshooting Reference

If you encounter a "404 Not Found nginx/1.29.0" error while accessing your deployed FastAPI backend, here are possible causes and resolutions:

### 1. Nginx Not Forwarding Requests Properly
Make sure nginx is configured to forward requests to the FastAPI application (via gunicorn, uvicorn, or similar). Relevant config for a typical FastAPI backend:

```nginx
server {
    listen 80;
    server_name mydomain.com;

    location / {
        proxy_pass http://localhost:8000;  # or the port your backend runs on
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/static/;  # static file support if needed
    }
}
```

### 2. Backend Not Running or Running on Wrong Port
Verify your `main.py` backend is started and accessible on the specified port. The default for uvicorn is `8000`.

### 3. Wrong Root Path (FastAPI root_path or sub-path deployments)
If your API is deployed behind a subpath (e.g. `/api/`), you must configure FastAPI with `root_path="/api"` and match that in your nginx config.

### 4. Static File/Frontend Asset Routing
For SPAs (React), nginx should serve `index.html` for frontend routes and forward API calls to backend.

### 5. File/Socket Permissions
If using a unix socket for gunicorn/uvicorn, ensure permissions are correct.
----
## Default Admin/Test User for Login

- On database seeding, the following admin user is always present:
    - **Email:** admin@example.com
    - **Password:** admin123

If you have trouble logging in as admin, run the following from the backend root to forcibly reseed and reset the admin credentials:

```bash
python -m sports_gear_backend.src.api.seed_data
```

The backend will always set the admin user to the password above during seed (for development/troubleshooting).

----

## Example Gunicorn/Uvicorn Launch

```bash
uvicorn sports_gear_backend.main:app --host 0.0.0.0 --port 8000
```

For production, consider using a process manager (gunicorn + uvicorn worker, systemd, supervisord, etc).
----
## Default Admin/Test User for Login

- On database seeding, the following admin user is always present:
    - **Email:** admin@example.com
    - **Password:** admin123

If you have trouble logging in as admin, run the following from the backend root to forcibly reseed and reset the admin credentials:

```bash
python -m sports_gear_backend.src.api.seed_data
```

The backend will always set the admin user to the password above during seed (for development/troubleshooting).

----

## Seeding the Product Catalog for Development

To populate the catalog with example data for shirts, trousers, and watches, you can run the following scripts from the `sports_gear_backend` directory:

```bash
python seed_shirts.py
python seed_trousers.py
python seed_watches.py
```

- Each script will insert 10 example products of the respective category into your local development database.
- Ensure the database is accessible before running these scripts.
----
## Default Admin/Test User for Login

- On database seeding, the following admin user is always present:
    - **Email:** admin@example.com
    - **Password:** admin123

If you have trouble logging in as admin, run the following from the backend root to forcibly reseed and reset the admin credentials:

```bash
python -m sports_gear_backend.src.api.seed_data
```

The backend will always set the admin user to the password above during seed (for development/troubleshooting).

----
