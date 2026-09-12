from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional, Dict
from app.db.session import get_db
from app.models.college import College
from app.schemas.college import CollegeList, CollegeDetail

router = APIRouter()

@router.get("/", response_model=Dict)
async def list_colleges(
    search: Optional[str] = None,
    location: Optional[str] = None,
    min_fees: Optional[int] = None,
    max_fees: Optional[int] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db)
):
    query = db.query(College)

    if search:
        query = query.filter(College.name.ilike(f"%{search}%"))
    if location:
        query = query.filter(College.location.ilike(f"%{location}%"))
    if min_fees:
        query = query.filter(College.fees >= min_fees)
    if max_fees:
        query = query.filter(College.fees <= max_fees)

    total = query.count()
    items = query.offset((page - 1) * limit).limit(limit).all()

    return {
        "status": "success",
        "data": {
            "items": items,
            "pagination": {
                "total": total,
                "page": page,
                "pages": (total + limit - 1) // limit
            }
        }
    }

@router.get("/{college_id}", response_model=CollegeDetail)
async def get_college(college_id: str, db: Session = Depends(get_db)):
    college = db.query(College).filter(College.id == college_id).first()
    if not college:
        raise HTTPException(status_code=404, detail="College not found")
    return college
