from app.schemas.rating_schema import RatingRequest, RatingResponse
from app.models.rating_model import Rating
from app.repositories.rating_repository import RatingRepository
from app.llm.prompt_builder import build_rating_prompt
from app.llm.llm_client import call_llm
from app.llm.output_parser import parse_llm_output


class RatingService:

    def __init__(self):

        self.repo = RatingRepository()

    def evaluate_rating(self, data: RatingRequest) -> RatingResponse:

        rating = Rating(
            dm_id=data.dm_id,
            reporter_id=data.reporter_id,
            dm_teaching_rating=data.dm_teaching_rating,
            reporter_learning_rating=data.reporter_learning_rating
        )

        self.repo.save(rating)

        prompt = build_rating_prompt(
            rating.dm_teaching_rating,
            rating.reporter_learning_rating
        )

        llm_output = call_llm(prompt)

        parsed = parse_llm_output(llm_output)

        return RatingResponse(
            dm_id=rating.dm_id,
            reporter_id=rating.reporter_id,
            ai_efficiency_score=parsed["efficiency_score"],
            feedback=parsed["feedback"]
        )