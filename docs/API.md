# Flask Starter API Documentation

Complete API reference for the Flask Starter application.

## Base URL

```
Development: http://localhost:5000/api/v1
Production:  https://your-domain.com/api/v1
```

## Authentication

Most endpoints require JWT authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your_access_token>
```

## Response Format

All API responses follow this structure:

### Success Response
```json
{
  "success": true,
  "data": { ... },
  "message": "Optional message"
}
```

### Error Response
```json
{
  "success": false,
  "error": "Error message",
  "errors": { ... }
}
```

---

## Authentication Endpoints

### Register New User

```http
POST /api/v1/auth/register
```

**Request Body:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response (201):**
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "is_admin": false,
    "created_at": "2026-02-02T12:00:00Z"
  },
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Login

```http
POST /api/v1/auth/login
```

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "SecurePass123!"
}
```

**Response (200):**
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com"
  },
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Get Current User

```http
GET /api/v1/auth/me
Authorization: Bearer <token>
```

**Response (200):**
```json
{
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "is_admin": false,
    "created_at": "2026-02-02T12:00:00Z"
  }
}
```

### Refresh Token

```http
POST /api/v1/auth/refresh
Authorization: Bearer <token>
```

**Response (200):**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Logout

```http
POST /api/v1/auth/logout
Authorization: Bearer <token>
```

**Response (200):**
```json
{
  "message": "Logout successful"
}
```

---

## User Endpoints

### List All Users

```http
GET /api/v1/users
```

**Response (200):**
```json
[
  {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "is_admin": false,
    "created_at": "2026-02-02T12:00:00Z"
  }
]
```

### Get User by ID

```http
GET /api/v1/users/:id
```

**Response (200):**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "is_admin": false,
  "created_at": "2026-02-02T12:00:00Z"
}
```

**Response (404):**
```json
{
  "error": "User not found"
}
```

### Update User

```http
PUT /api/v1/users/:id
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "first_name": "Jane",
  "last_name": "Smith",
  "email": "jane@example.com"
}
```

**Response (200):**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "jane@example.com",
  "first_name": "Jane",
  "last_name": "Smith",
  "is_admin": false,
  "updated_at": "2026-02-02T13:00:00Z"
}
```

### Delete User

```http
DELETE /api/v1/users/:id
Authorization: Bearer <token>
```

**Response (204): No Content**

---

## Post Endpoints

### List All Posts

```http
GET /api/v1/posts
```

**Query Parameters:**
- `page` (optional): Page number (default: 1)
- `per_page` (optional): Items per page (default: 10)

**Response (200):**
```json
[
  {
    "id": 1,
    "title": "My First Post",
    "content": "This is the post content",
    "summary": "A brief summary",
    "published": true,
    "user_id": 1,
    "created_at": "2026-02-02T12:00:00Z"
  }
]
```

### Get Post by ID

```http
GET /api/v1/posts/:id
```

**Response (200):**
```json
{
  "id": 1,
  "title": "My First Post",
  "content": "This is the post content",
  "summary": "A brief summary",
  "published": true,
  "user_id": 1,
  "created_at": "2026-02-02T12:00:00Z"
}
```

### Create Post

```http
POST /api/v1/posts
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "title": "My New Post",
  "content": "Post content goes here",
  "summary": "Optional summary",
  "published": true
}
```

**Response (201):**
```json
{
  "id": 2,
  "title": "My New Post",
  "content": "Post content goes here",
  "summary": "Optional summary",
  "published": true,
  "user_id": 1,
  "created_at": "2026-02-02T13:00:00Z"
}
```

### Update Post

```http
PUT /api/v1/posts/:id
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "title": "Updated Title",
  "content": "Updated content",
  "published": false
}
```

**Response (200):**
```json
{
  "id": 1,
  "title": "Updated Title",
  "content": "Updated content",
  "summary": "A brief summary",
  "published": false,
  "user_id": 1,
  "updated_at": "2026-02-02T14:00:00Z"
}
```

### Delete Post

```http
DELETE /api/v1/posts/:id
Authorization: Bearer <token>
```

**Response (204): No Content**

---

## Health Check

```http
GET /health
```

**Response (200):**
```json
{
  "status": "healthy",
  "version": "v1"
}
```

---

## Error Codes

| Code | Description |
|------|-------------|
| 200  | Success |
| 201  | Created |
| 204  | No Content |
| 400  | Bad Request |
| 401  | Unauthorized |
| 403  | Forbidden |
| 404  | Not Found |
| 415  | Unsupported Media Type |
| 500  | Internal Server Error |

---

## Rate Limiting

API endpoints are rate-limited to prevent abuse:

- 100 requests per minute per IP
- 1000 requests per hour per IP

Rate limit headers are included in responses:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1643844600
```

---

## Pagination

List endpoints support pagination:

**Query Parameters:**
- `page`: Page number (default: 1)
- `per_page`: Items per page (default: 10, max: 100)

**Response Headers:**
```
X-Total-Count: 250
X-Total-Pages: 25
X-Current-Page: 1
X-Per-Page: 10
```

---

## Interactive Documentation

Interactive API documentation is available:

- **Swagger UI**: `http://localhost:5000/api/v1/docs`
- **ReDoc**: `http://localhost:5000/api/v1/redoc`

---

## SDK Examples

### Python

```python
import requests

# Login
response = requests.post('http://localhost:5000/api/v1/auth/login', json={
    'username': 'johndoe',
    'password': 'SecurePass123!'
})
token = response.json()['access_token']

# Get posts
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('http://localhost:5000/api/v1/posts', headers=headers)
posts = response.json()
```

### JavaScript

```javascript
// Login
const response = await fetch('http://localhost:5000/api/v1/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    username: 'johndoe',
    password: 'SecurePass123!'
  })
})
const { access_token } = await response.json()

// Get posts
const posts = await fetch('http://localhost:5000/api/v1/posts', {
  headers: { 'Authorization': `Bearer ${access_token}` }
}).then(r => r.json())
```

### cURL

```bash
# Login
TOKEN=$(curl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"johndoe","password":"SecurePass123!"}' \
  | jq -r '.access_token')

# Get posts
curl http://localhost:5000/api/v1/posts \
  -H "Authorization: Bearer $TOKEN"
```
