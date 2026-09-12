# 🛰️ College Discovery Platform - API Specification (v1.0)

This document serves as the official API contract for the College Discovery Backend.

## 📋 API Overview
- **Base URL:** `http://localhost:8000/api/v1`
- **Protocol:** HTTPS / REST
- **Auth:** Bearer Token (JWT)
- **Documentation:** `/docs` (Swagger UI)

---

## 🏫 College Management

### 1. List Colleges
`GET /colleges`

Fetches a list of colleges with support for search, filtering, and pagination.

**Request:**
- `query` params:
    - `search`: string (optional)
    - `location`: string (optional)
    - `min_fees`: int (optional)
    - `max_fees`: int (optional)
    - `page`: int (default: 1)

**Success Response (200 OK):**
```json
{
  "status": "success",
  "data": {
    "items": [
      {
        "id": "c101",
        "name": "Institute of Technology, Delhi",
        "location": "New Delhi",
        "fees": 250000,
        "rating": 4.9,
        "thumbnail": "https://cdn.example.com/iitd.png"
      }
    ],
    "pagination": {
      "total": 540,
      "page": 1,
      "pages": 54
    }
  }
}
```

---

### 2. Get College Details
`GET /colleges/{id}`

Retrieve full metadata for a specific college including nested resources.

**Success Response (200 OK):**
```json
{
  "id": "c101",
  "name": "Institute of Technology, Delhi",
  "overview": "Premier engineering institute in India...",
  "location": "New Delhi",
  "placement_stats": {
    "avg_package": "22 LPA",
    "highest_package": "1.2 Cr",
    "placement_rate": "98%"
  },
  "courses": [
    { "name": "B.Tech Computer Science", "duration": "4 Years" },
    { "name": "B.Tech Mechanical", "duration": "4 Years" }
  ],
  "reviews": [
    { "user": "Aryan", "rating": 5, "comment": "Excellent faculty." }
  ]
}
```

---

## 📊 Analytics & Tools

### 3. Compare Colleges
`POST /compare`

Compare multiple colleges side-by-side based on their IDs.

**Request Body:**
```json
{
  "college_ids": ["c101", "c102", "c103"]
}
```

**Success Response (200 OK):**
```json
{
  "comparison_matrix": [
    {
      "metric": "Annual Fees",
      "c101": 250000,
      "c102": 210000
    },
    {
      "metric": "Avg Placement",
      "c101": "22 LPA",
      "c102": "18 LPA"
    }
  ]
}
```

---

### 4. Admission Predictor
`POST /predictor`

Predicts admission chances based on rank and exam type.

**Request Body:**
```json
{
  "exam": "JEE Main",
  "rank": 1500,
  "category": "General"
}
```

**Success Response (200 OK):**
```json
{
  "results": [
    {
      "college_id": "c105",
      "name": "NIT Trichy",
      "branch": "Computer Science",
      "chance": "High"
    },
    {
      "college_id": "c101",
      "name": "IIT Delhi",
      "branch": "Textile Engineering",
      "chance": "Low"
    }
  ]
}
```

---

## ⚠️ Error Responses

| Code | Description | Example Detail |
| :--- | :--- | :--- |
| `400` | Bad Request | "Invalid college ID format" |
| `401` | Unauthorized | "JWT Token expired" |
| `404` | Not Found | "College with ID c999 not found" |
| `422` | Validation Error | "Rank must be a positive integer" |

**Generic Error Format:**
```json
{
  "error": {
    "code": "ENTITY_NOT_FOUND",
    "message": "The requested college does not exist."
  }
}
```
