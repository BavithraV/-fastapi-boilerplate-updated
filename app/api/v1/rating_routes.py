from fastapi import APIRouter
from app.schemas.rating_schema import RatingRequest, RatingResponse
from app.services.rating_service import RatingService

router = APIRouter(prefix="/ratings", tags=["ratings"])

service = RatingService()


@router.post("/", response_model=RatingResponse)
def create_rating(payload: RatingRequest):
    """
    Create and evaluate a DM–Reporter rating.

    This endpoint receives rating information about how effectively
    a District Manager (DM) teaches and how efficiently a Reporter
    learns. The input ratings are processed by the service layer,
    which sends them to an AI model for evaluation.

    The AI returns:
    - an efficiency score
    - qualitative feedback describing the training effectiveness

    Args:
        payload (RatingRequest):
            Request body containing:
            - dm_id
            - reporter_id
            - dm_teaching_rating
            - reporter_learning_rating

    Returns:
        RatingResponse:
            Contains the AI-generated efficiency score and feedback.
    """
    result = service.evaluate_rating(payload)

    return result