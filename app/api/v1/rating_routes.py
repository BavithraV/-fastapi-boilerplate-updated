from fastapi import APIRouter
from app.schemas.rating_schema import RatingRequest, RatingResponse
from app.services.rating_service import RatingService

router = APIRouter(prefix="/ratings", tags=["ratings"])

service = RatingService()


@router.post("/", response_model=RatingResponse)
def create_rating(payload: RatingRequest):

    result = service.evaluate_rating(payload)

    return result