from dataclasses import dataclass


@dataclass
class Rating:

    dm_id: int
    reporter_id: int
    dm_teaching_rating: float
    reporter_learning_rating: float