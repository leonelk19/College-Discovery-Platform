# 🎓 College Discovery Platform

A full-stack application for discovering, comparing, and predicting college admissions.

## 🛠️ Tech Stack

- **Frontend:** Next.js (React, Tailwind CSS, TypeScript)
- **Backend:** FastAPI (Python, SQLAlchemy, Pydantic)
- **Database:** PostgreSQL
- **Infrastructure:** Railway/Render, Neon

## 📂 Project Structure

- `/frontend`: Next.js web application.
- `/backend`: FastAPI backend service.
- `/.artifacts`: API specifications, SRS, and architecture documents.

## 🚀 Getting Started

### Backend (FastAPI)
1. Navigate to `/backend`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the server: `python main.py` or `uvicorn main:app --reload`.

## ☁️ Deployment (Render)

### Option 1: Automatic (Blueprint)
1. **GitHub:** Push your code to a GitHub repository.
2. **Render:** Log in to [Render](https://render.com/).
3. **Blueprint:** Click **"New +"** and select **"Blueprint"**.
4. **Connect:** Connect your GitHub repository. Render will automatically detect the `render.yaml` and set everything up.

### Option 2: Manual (Web Service)
If you are setting up the service manually, use these EXACT settings:
- **Root Directory:** `backend`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Environment Variables:** Add `DATABASE_URL` from your Render PostgreSQL instance.

## 📜 API Specification
See the [API Specification](.artifacts/789d3e8c-854d-4f6d-9e5d-3a879c177a0e/api_specification.artifact.md) for detailed endpoint documentation.
