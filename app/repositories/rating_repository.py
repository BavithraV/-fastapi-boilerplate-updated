from typing import List
from app.models.rating_model import Rating


class RatingRepository:

    def __init__(self):
        self.storage: List[Rating] = []

    def save(self, rating: Rating):

        self.storage.append(rating)

        return rating