from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Dict

class CollegeBase(BaseModel):
    name: str
    location: str
    fees: int
    rating: float
    thumbnail: Optional[str] = None

class CollegeCreate(CollegeBase):
    overview: str
    placement_stats: Dict

class CollegeList(CollegeBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

class CourseSchema(BaseModel):
    name: str
    duration: str
    model_config = ConfigDict(from_attributes=True)

class ReviewSchema(BaseModel):
    user_name: str
    rating: int
    comment: str
    model_config = ConfigDict(from_attributes=True)

class CollegeDetail(CollegeList):
    overview: str
    placement_stats: Dict
    courses: List[CourseSchema] = []
    reviews: List[ReviewSchema] = []
    model_config = ConfigDict(from_attributes=True)

class CollegeCompareRequest(BaseModel):
    college_ids: List[str]

class PredictorRequest(BaseModel):
    exam: str
    rank: int
    category: str
