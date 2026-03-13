from app.services.rating_service import RatingService
from app.schemas.rating_schema import RatingRequest


def test_rating_service_with_mock(mocker):

    mocker.patch(
        "app.services.rating_service.call_llm",
        return_value='{"efficiency_score": 8.5, "feedback": "Good learning efficiency"}'
    )

    service = RatingService()

    request = RatingRequest(
        dm_id=1,
        reporter_id=2,
        dm_teaching_rating=8,
        reporter_learning_rating=7
    )

    result = service.evaluate_rating(request)

    assert result.ai_efficiency_score == 8.5
    assert result.feedback == "Bad learning efficiency"