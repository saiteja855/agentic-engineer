# URL Shortener API
=====================================

## Project Overview
-------------------

The URL Shortener API is a web application that allows users to shorten long URLs and share them with others. The API provides endpoints for creating, reading, updating, and deleting (CRUD) URLs.

## Features
------------

*   **URL Shortening**: Users can submit a long URL and receive a shortened version.
*   **Redirects**: When a user visits the shortened URL, they are redirected to the original long URL.
*   **Statistics**: The API provides statistics about each URL, including the number of redirects.

## Folder Structure
-------------------

The project follows a modular structure with separate modules for database interactions (`database.py`), data models (`models.py`), API routing (`routes.py`), and configuration (`main.py`).

## Installation
--------------

To install the dependencies required by the application, run the following command:

```bash
pip install -r requirements.txt
```

## Running Application
----------------------

To start the application, execute the following command in your terminal:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Endpoints
----------------

### URL Shortening

*   **POST /shorten**: Accepts a long URL as input and generates a unique short URL for redirection.
    *   Request Body:
        ```json
{
    "long_url": "https://www.example.com/very-long-url"
}
```
    *   Response:
        ```json
{
    "short_code": "abc123"
}
```

### Redirects

*   **GET /{short_code}**: Redirects to the original long URL associated with the provided short code.
    *   Example Request:
        ```bash
curl http://localhost:8000/abc123
```
    *   Response:
        ```http
HTTP 302 Found
Location: https://www.example.com/very-long-url
```

### Statistics

*   **GET /stats/{short_code}**: Returns statistics about the URL, including the number of redirects.
    *   Example Request:
        ```bash
curl http://localhost:8000/stats/abc123
```
    *   Response:
        ```json
{
    "click_count": 10
}
```

## Example Requests
--------------------

### Shorten a URL

```bash
curl -X POST \
  http://localhost:8000/shorten \
  -H 'Content-Type: application/json' \
  -d '{"long_url": "https://www.example.com/very-long-url"}'
```

### Redirect to a shortened URL

```bash
curl http://localhost:8000/abc123
```

### Get statistics for a shortened URL

```bash
curl http://localhost:8000/stats/abc123