# ManStyle Hub Backend API Documentation

This document provides REST API reference for the **ManStyle Hub** men's fashion & accessories backend.

- **Platform**: FastAPI
- **Location**: `sports_gear_backend`
- **OpenAPI/Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **OpenAPI JSON**: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

> **Note:** The endpoints described are for a men's apparel and accessory shop. Examples reference categories like shirts, jackets, shoes, belts, and more—not sports gear.

---

## Table of Contents

- [Health & Database Endpoints](#health--database-endpoints)
- [User Management & Auth](#user-management--auth)
- [Product Catalog](#product-catalog)
- [Shopping Cart](#shopping-cart)
- [Checkout (Stripe)](#checkout-stripe)
- [Order Management](#order-management)

---

## Health & Database Endpoints

### `GET /`
**Description:** General health check.
- **Response:**
    - `200 OK`: `{"message": "Healthy"}`

### `GET /db/health`
**Description:** Tests database connectivity.
- **Responses:**
    - `200 OK`: `{"db_health": "ok"}`
    - `503 Service Unavailable`: `{"db_health": "unavailable", "detail": "<error details>"}`

---

## User Management & Auth

### `POST /auth/register`
**Description:** Register a new user.
- **Request body:**
    ```json
    {
        "email": "user@example.com",
        "password": "string (min 6 chars)",
        "full_name": "optional"
    }
    ```
- **Responses:**
    - `201 Created` (example):
        ```json
        {
            "id": 1,
            "email": "user@example.com",
            "full_name": "Test User",
            "is_active": true,
            "created_at": "2024-01-01T12:00:00"
        }
        ```
    - `409 Conflict`: `{"detail": "Email already registered"}`
    - `400 Bad Request`: `{"detail": "Could not create user"}`

### `POST /auth/login`
**Description:** Login endpoint (OAuth2).  
**Request Encoding:** `application/x-www-form-urlencoded`  
**Form fields:**
- `username` (email)
- `password`

- **Responses:**
    - `200 OK`:
        ```json
        {
            "access_token": "<JWT>",
            "token_type": "bearer"
        }
        ```
    - `400 Bad Request`: `{"detail": "Invalid email or password"}`

### `GET /users/me`
**Description:** Get current user's profile.  
**Authorization:** Bearer token required.
- **Response:**
    - `200 OK`: User profile as above

### `PUT /users/me`
**Description:** Update current user's profile  
**Authorization:** Bearer token required.
- **Request body:**
    ```json
    {
        "full_name": "optional",
        "password": "optional (min 6 chars)"
    }
    ```
- **Response:**
    - `200 OK`: Updated user profile

---

## Product Catalog

### `GET /categories`
**Description:** List all product categories.

- **Response:**
    ```json
    [
        {
            "id": 1,
            "name": "Shoes",
            "description": "Footwear and sports shoes"
        },
        ...
    ]
    ```

### `GET /products`
**Description:** List/search products.  
**Query Parameters:**
- `q` (string): Search keyword
- `category_id` (int): Filter by category
- `size` (string): Filter by size (comma-separated for multi-size)

- **Response:**
    ```json
    [
        {
            "id": 12,
            "name": "Soccer Ball",
            "description": "High quality ball",
            "image_url": "https://...",
            "price": 30.0,
            "available_sizes": "M,L",
            "category": {
                "id": 3,
                "name": "Balls",
                "description": null
            }
        },
        ...
    ]
    ```

### `GET /products/{product_id}`
**Description:** Get a single product's details by ID.

- **Response:**
    - `200 OK`: (as above for single product)
    - `404 Not Found`: `{"detail": "Product not found"}`

---

## Shopping Cart

**All cart endpoints require user authentication (Bearer token).**

### `GET /cart`
**Description:** Get current user's shopping cart.

- **Response:**
    ```json
    {
        "id": 7,
        "items": [
            {
                "id": 1,
                "product": {
                    "id": 12,
                    "name": "Soccer Ball",
                    "description": "...",
                    "image_url": "...",
                    "price": 30.0,
                    "available_sizes": "M,L",
                    "category": {...}
                },
                "quantity": 2,
                "selected_size": "M"
            }
        ],
        "created_at": "2024-01-01T11:05:27",
        "checked_out": false
    }
    ```

### `POST /cart/items`
**Description:** Add item to cart.
- **Request body:**
    ```json
    {
        "product_id": 12,
        "quantity": 1,
        "selected_size": "M"
    }
    ```
- **Response:** Updated cart (see above)
- **Errors:**
    - `404 Not Found`: `{"detail": "Product not found"}`

### `PUT /cart/items/{cart_item_id}`
**Description:** Update a cart item's quantity/size.
- **Request body:**
    ```json
    {
        "product_id": 12,
        "quantity": 2,
        "selected_size": "L"
    }
    ```
- **Response:** Updated cart
- **Errors:**
    - `404 Not Found`: `{"detail": "Cart item not found"}`

### `DELETE /cart/items/{cart_item_id}`
**Description:** Remove item from cart.
- **Response:** Updated cart
- **Errors:**
    - `404 Not Found`: `{"detail": "Cart item not found"}`

---

## Checkout (Stripe)

**All checkout endpoints require user authentication.**

### `POST /checkout/stripe-session`
**Description:** Create Stripe checkout session for current cart.
- **Response:**
    - `200 OK`:
      ```json
      {
          "checkout_url": "https://checkout.stripe.com/..."
      }
      ```
    - `400 Bad Request`: `{"detail": "No items in cart"}`
    - `500 Internal Server Error`: Stripe-related errors

### `POST /checkout/complete`
**Description:** Complete checkout ("simulate payment"), creates an order, empties cart.  
- **Response:**
    - `200 OK`:
      ```json
      {
          "id": 5,
          "created_at": "2024-01-01T11:22:10",
          "total_amount": 57.20,
          "status": "paid",
          "order_items": [
            {
                "id": 1,
                "product": { ... },
                "quantity": 2,
                "price_at_purchase": 28.60,
                "selected_size": "M"
            }
          ]
      }
      ```
    - `400 Bad Request`: `{"detail": "No items in cart"}`

---

## Order Management

**All order endpoints require user authentication.**

### `GET /orders`
**Description:** Get current user's order history.
- **Response:** List of orders (see above for structure).

### `GET /orders/{order_id}`
**Description:** Get a specific order by ID.
- **Response:** Order as above  
- **Error:** `404 Not Found`: `{"detail": "Order not found"}`

---

## API Schema Reference (OpenAPI/Swagger)

This backend exposes OpenAPI schema at:  
[`/openapi.json`](http://localhost:8000/openapi.json)  
which you can import into tools like Swagger UI or Postman.

- **Live Interactive Docs:**  
  [`/docs`](http://localhost:8000/docs) ([Swagger UI], try out all endpoints)

---

## Authentication

Most endpoints require a Bearer token; acquire it by logging in at `/auth/login` and using the returned `access_token`.

Example Authorization header:
```
Authorization: Bearer <access_token>
```

---

## Error Cases

- **404 Not Found**: Returned when a referenced resource does not exist (products, cart items, order, etc).
- **400 Bad Request**: Input validation error, or failing precondition (e.g., No items in cart).
- **401 Unauthorized**: Accessing a protected endpoint without or with invalid/expired token.
- **409 Conflict**: Uniqueness/duplicate errors (e.g., email already registered).
- **503 Service Unavailable**: Database inaccessible/failed health check.
- **500 Internal Server Error**: Uncaught backend or Stripe error.

---

## Example Entities

### User
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "Test User",
  "is_active": true,
  "created_at": "2024-01-01T12:00:00"
}
```
### Product
```json
{
  "id": 1,
  "name": "Soccer Shoes",
  "description": "Durable shoes",
  "image_url": "http://...",
  "price": 90.0,
  "available_sizes": "M,L,XL",
  "category": {
    "id": 1,
    "name": "Footwear",
    "description": "Shoes, boots"
  }
}
```
---

## Notes

- All endpoints with `current_user: models.User = Depends(get_current_active_user)` require authentication.
- All entity ID values are integers; timestamps are ISO8601.

---

## OpenAPI/Swagger Schema (Auto-generated)

This backend's full OpenAPI/Swagger schema is always live at [`/openapi.json`](http://localhost:8000/openapi.json).  
No separate OpenAPI YAML is included here since it is generated from the actual FastAPI app and can be accessed/downloaded at runtime.

---
