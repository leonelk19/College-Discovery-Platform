from sqlalchemy import Column, String, Integer, Float, Text, JSON
from sqlalchemy.orm import relationship
from app.db.session import Base

class College(Base):
    __tablename__ = "colleges"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    location = Column(String, index=True)
    fees = Column(Integer)
    rating = Column(Float, index=True)
    overview = Column(Text)
    placement_stats = Column(JSON)  # Stores avg_package, highest_package, etc.
    thumbnail = Column(String)

    courses = relationship("Course", back_populates="college")
    reviews = relationship("Review", back_populates="college")
