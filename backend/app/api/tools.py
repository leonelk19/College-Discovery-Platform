from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.college import College
from app.schemas.college import CollegeCompareRequest, PredictorRequest

router = APIRouter()

@router.post("/compare")
async def compare_colleges(request: CollegeCompareRequest, db: Session = Depends(get_db)):
    colleges = db.query(College).filter(College.id.in_(request.college_ids)).all()

    metrics = ["Annual Fees", "Avg Placement", "Rating"]
    matrix = []

    for metric in metrics:
        row = {"metric": metric}
        for c in colleges:
            if metric == "Annual Fees":
                row[c.id] = c.fees
            elif metric == "Avg Placement":
                row[c.id] = c.placement_stats.get("avg_package", "N/A")
            elif metric == "Rating":
                row[c.id] = c.rating
        matrix.append(row)

    return {"comparison_matrix": matrix}

@router.post("/predictor")
async def admission_predictor(request: PredictorRequest):
    recommendations = [
        {
            "college_id": "c105",
            "name": "NIT Trichy",
            "branch": "Computer Science",
            "chance": "High" if request.rank < 2000 else "Medium"
        },
        {
            "college_id": "c101",
            "name": "IIT Delhi",
            "branch": "Textile Engineering",
            "chance": "Low" if request.rank > 1000 else "Medium"
        }
    ]
    return {"results": recommendations}
