from typing import List
from app.models.rating_model import Rating


class RatingRepository:
    """
    Repository layer responsible for managing Rating data storage.

    This repository acts as a data access layer between the service layer
    and the underlying storage mechanism. In this implementation, ratings
    are stored temporarily in an in-memory list.

    In a production system, this repository could be extended to interact
    with a real database such as PostgreSQL, MongoDB, or Redis.
    """
    def __init__(self):
        """
        Initialize the repository with an empty in-memory storage.

        The storage is represented as a list that holds Rating objects.
        """        
        self.storage: List[Rating] = []

    def save(self, rating: Rating):
        """
        Save a Rating object to the repository.

        This method appends the provided Rating instance to the in-memory
        storage list.

        Args:
            rating (Rating):
                The Rating object containing DM and Reporter rating details.

        Returns:
            Rating:
                The same Rating object that was stored.
        """

        self.storage.append(rating)

        return rating