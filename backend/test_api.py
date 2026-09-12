import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import Base, get_db
from main import app

# Import all models before creating tables so their metadata is registered.
from app.models.college import College
from app.models.course import Course
from app.models.review import Review

# Use a local SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
if os.path.exists("./test.db"):
    os.remove("./test.db")

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_seed_and_apis():
    # 1. Seed the test database logic
    from app.models.college import College
    from app.models.course import Course
    from app.models.review import Review

    db = TestingSessionLocal()

    # Add dummy data
    iitd = College(
        id="c101",
        name="IIT Delhi",
        location="New Delhi",
        fees=250000,
        rating=4.9,
        overview="Top Tier",
        placement_stats={"avg_package": "22 LPA"},
        thumbnail="http://example.com/thumb.png"
    )
    db.add(iitd)
    db.add(Course(id="crs1", name="CS", duration="4y", college_id="c101"))
    db.add(Review(id="r1", user_name="Aryan", rating=5, comment="Good", college_id="c101"))
    db.commit()
    db.close()

    print("\n--- Testing GET /api/v1/colleges ---")
    response = client.get("/api/v1/colleges/")
    print(f"Status: {response.status_code}")
    print(f"Body: {response.json()}")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

    print("\n--- Testing GET /api/v1/colleges/c101 ---")
    response = client.get("/api/v1/colleges/c101")
    print(f"Status: {response.status_code}")
    print(f"Body: {response.json()}")
    assert response.status_code == 200
    assert response.json()["name"] == "IIT Delhi"

    print("\n--- Testing POST /api/v1/compare ---")
    response = client.post("/api/v1/compare", json={"college_ids": ["c101"]})
    print(f"Status: {response.status_code}")
    print(f"Body: {response.json()}")
    assert response.status_code == 200
    assert "comparison_matrix" in response.json()

    print("\n--- Testing POST /api/v1/predictor ---")
    response = client.post("/api/v1/predictor", json={"exam": "JEE", "rank": 500, "category": "General"})
    print(f"Status: {response.status_code}")
    print(f"Body: {response.json()}")
    assert response.status_code == 200
    assert "results" in response.json()

if __name__ == "__main__":
    try:
        test_seed_and_apis()
        print("\n✅ All tests passed successfully!")
    finally:
        # Cleanup
        if os.path.exists("./test.db"):
            os.remove("./test.db")
