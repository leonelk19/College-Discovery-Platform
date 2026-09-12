from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.session import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(String, primary_key=True, index=True)
    user_name = Column(String)
    rating = Column(Integer)
    comment = Column(Text)
    college_id = Column(String, ForeignKey("colleges.id"))

    college = relationship("College", back_populates="reviews")
