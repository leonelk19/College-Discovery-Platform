# 📄 Software Requirements Specification (SRS)
**Project:** College Discovery Platform (Backend MVP)
**Role:** Backend Engineer
**Tech Stack:** FastAPI (Python), PostgreSQL, SQLAlchemy, Pydantic, Railway/Render, Neon

---

## 1. Introduction
- **Purpose:** Provide a robust backend system enabling college discovery, detail exploration, and comparison for students.
- **Scope:** High-performance RESTful APIs for listing, searching, filtering, and comparing colleges; database schema design; validation and reliability mechanisms.
- **Audience:** Students (end users), Frontend Engineers (Next.js), and Technical Evaluators.

---

## 2. System Features

### 2.1 College Listing API
- **Endpoint:** `GET /api/colleges`
- **Features:**
  - Dynamic Filters: `location`, `fees_range`, `min_rating`
  - Pagination: `page`, `limit` (default: 10)
  - Sorting: `rating` (desc), `fees` (asc/desc)
- **Validation:** Pydantic models for query parameter verification.

### 2.2 College Detail API
- **Endpoint:** `GET /api/colleges/{id}`
- **Features:**
  - Returns deep-dive data: campus overview, specific courses, placement stats, and user reviews.
- **Data Integrity:** Foreign key constraints ensuring Course and Review data consistency.

### 2.3 College Comparison API
- **Endpoint:** `POST /api/compare`
- **Features:**
  - Input: List of unique College IDs.
  - Output: Parallel JSON structure for side-by-side comparison of fees, average package, and ratings.

### 2.4 Admission Predictor (Advanced Mock)
- **Endpoint:** `POST /api/predictor`
- **Features:**
  - Input: `exam_name`, `rank`, `category`.
  - Logic: Returns a list of probable colleges based on historical cut-off ranges.

---

## 3. Database Schema (PostgreSQL)
- **College:** `(id, name, location, fees, rating, overview, placement_json, thumbnail_url)`
- **Course:** `(id, name, duration, college_id)`
- **Review:** `(id, user_id, rating, comment, college_id)`
- **User:** `(id, email, password_hash, created_at)`

---

## 4. Engineering Standards
- **Validation:** Pydantic v2 for strict type checking and auto-documentation.
- **Reliability:** Middleware for Global Exception Handling and standardized error responses.
- **Documentation:** Automatic OpenAPI/Swagger generation via FastAPI.
- **Performance:** Asynchronous DB operations (asyncio) for high concurrency.

---

## 5. Deployment & DevOps
- **Hosting:** Railway/Render for the API service.
- **Database:** Neon Serverless Postgres for scalability.
- **Environment Management:** `.env` driven configuration for DB secrets and API keys.
