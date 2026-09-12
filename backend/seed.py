from app.db.session import SessionLocal, Base, engine
from app.models.college import College
from app.models.course import Course
from app.models.review import Review

def seed_db():
    # Create tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Check if data already exists
    if db.query(College).first():
        print("Database already seeded.")
        return

    # Sample College
    iitd = College(
        id="c101",
        name="Institute of Technology, Delhi",
        location="New Delhi",
        fees=250000,
        rating=4.9,
        overview="Premier engineering institute in India offering world-class education and research opportunities.",
        placement_stats={
            "avg_package": "22 LPA",
            "highest_package": "1.2 Cr",
            "placement_rate": "98%"
        },
        thumbnail="https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&q=80&w=400"
    )

    # Sample Courses
    cs = Course(id="crs1", name="B.Tech Computer Science", duration="4 Years", college_id="c101")
    me = Course(id="crs2", name="B.Tech Mechanical", duration="4 Years", college_id="c101")

    # Sample Review
    rev = Review(id="r1", user_name="Aryan", rating=5, comment="Excellent faculty and peer group.", college_id="c101")

    db.add(iitd)
    db.add(cs)
    db.add(me)
    db.add(rev)

    db.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_db()
