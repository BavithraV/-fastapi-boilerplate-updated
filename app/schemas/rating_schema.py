from pydantic import BaseModel, Field


class RatingRequest(BaseModel):

    dm_id: int
    reporter_id: int

    dm_teaching_rating: float = Field(..., ge=1, le=10)
    reporter_learning_rating: float = Field(..., ge=1, le=10)


class RatingResponse(BaseModel):

    dm_id: int
    reporter_id: int

    ai_efficiency_score: float
    feedback: str