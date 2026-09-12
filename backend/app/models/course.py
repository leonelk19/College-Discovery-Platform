from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    duration = Column(String)
    college_id = Column(String, ForeignKey("colleges.id"))

    college = relationship("College", back_populates="courses")
