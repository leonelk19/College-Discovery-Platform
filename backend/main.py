from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.colleges import router as colleges_router
from app.api.tools import router as tools_router
from app.db.session import Base, engine

# Import models so SQLAlchemy registers all tables before schema creation
from app.models import college, course, review  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="College Discovery Platform API",
    description="Backend API for college listing, comparison, and prediction.",
    version="1.0.0",
)

# CORS configuration for Next.js frontend
origins = [
    "http://localhost:3000",
    "https://college-discovery-platform.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(colleges_router, prefix="/api/v1/colleges", tags=["Colleges"])
app.include_router(tools_router, prefix="/api/v1", tags=["Tools"])

@app.get("/")
async def root():
    return {"message": "Welcome to College Discovery Platform API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
