import uuid
from datetime import datetime
from typing import List, Optional

class Expense:
    def __init__(self, title: str, amount: float):
        """
        Initializes a new Expense instance.
        
        Args:
            title (str): The title/description of the expense.
            amount (float): The monetary amount of the expense.
        """
        self.id = str(uuid.uuid4())         # Unique identifier for the expense
        self.title = title
        self.amount = float(amount)
        self.created_at = datetime.utcnow()   # Timestamp in UTC when expense is created
        self.updated_at = self.created_at     # Initially, updated_at is the same as created_at

    def update(self, title: Optional[str] = None, amount: Optional[float] = None):
        """
        Updates the expense details. Only non-None values are updated.
        The updated_at timestamp is refreshed to the current UTC time.
        
        Args:
            title (Optional[str]): New title for the expense. If None, title remains unchanged.
            amount (Optional[float]): New amount for the expense. If None, amount remains unchanged.
        """
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = float(amount)
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the expense.
        Timestamps are formatted as ISO 8601 strings.
        
        Returns:
            dict: A dictionary with the expense's details.
        """
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat() + "Z",
            "updated_at": self.updated_at.isoformat() + "Z"
        }
