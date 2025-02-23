import uuid
from datetime import datetime
from typing import List,Optional,Union
from decimal import Decimal, InvalidOperation

class Expense:
    def __init__(self, title: str, amount: float):
        """
        Initializes a new Expense instance.
        
        Args:
            title (str): The title/description of the expense.
            amount (float): The monetary amount of the expense.
        
        Raises:
            ValueError: If the title is empty or amount is negative.
        """
        if not title:
            raise ValueError("Title cannot be empty.")
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        
        self.id = str(uuid.uuid4())         # Unique identifier for the expense
        self.title = title
        self.amount = Decimal(amount)
        self.created_at = datetime.utcnow()   # Timestamp in UTC when expense is created
        self.updated_at = self.created_at     # Initially, updated_at is the same as created_at

    def update(self, title: Optional[str] = None, amount: Optional[float] = None):
        """
        Updates the expense details. Only non-None values are updated.
        The updated_at timestamp is refreshed to the current UTC time.
        
        Args:
            title (Optional[str]): New title for the expense. If None, title remains unchanged.
            amount (Optional[float]): New amount for the expense. If None, amount remains unchanged.
        
        Raises:
            ValueError: If the title is empty or amount is negative.
        """
        if title is not None:
            if not title:
                raise ValueError("Title cannot be empty.")
            self.title = title
        if amount is not None:
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            try:
                self.amount = Decimal(amount)
            except InvalidOperation:
                raise ValueError("Invalid amount format.")
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
            "amount": float(self.amount),
            "created_at": self.created_at.isoformat() + "Z",
            "updated_at": self.updated_at.isoformat() + "Z"
        }

class ExpenseDatabase:
    def __init__(self):
        """
        Initializes the ExpenseDatabase with an empty list of expenses.
        """
        self.expenses: List[Expense] = []

    def add_expense(self, expense: Expense):
        """
        Adds a new Expense to the database.
        
        Args:
            expense (Expense): The expense object to add.
            
        Raises:
            TypeError: If the expense is not an instance of Expense.
        """
        if not isinstance(expense, Expense):
            raise TypeError("add_expense expects an Expense instance")
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str) -> bool:
        """
        Removes an expense from the database by its unique identifier.
        
        Args:
            expense_id (str): The unique identifier of the expense to remove.
            
        Returns:
            bool: True if an expense was removed, False if no matching expense was found.
        """
        initial_len = len(self.expenses)
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]
        # Check if any expense was removed by comparing list lengths.
        return len(self.expenses) < initial_len

    def get_expense_by_id(self, expense_id: str) -> Optional[Expense]:
        """
        Retrieves a single expense by its unique identifier.
        
        Args:
            expense_id (str): The unique identifier of the expense.
        
        Returns:
            Expense or None: The matching expense, or None if not found.
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, title: str) -> List[Expense]:
        """
        Retrieves all expenses with a matching title.
        
        Args:
            title (str): The title to search for.
        
        Returns:
            List[Expense]: A list of expenses with the given title.
            
        Raises:
            ValueError: If the title is an empty string.
        """
        if not title:
            raise ValueError("Title cannot be empty")
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self) -> List[dict]:
        """
        Returns a list of dictionary representations of all expenses in the database.
        
        Returns:
            List[dict]: List where each element is an expense represented as a dictionary.
        """
        return [expense.to_dict() for expense in self.expenses]

# Demonstration of functionality:
if __name__ == "__main__":
    # Create an instance of ExpenseDatabase
    db = ExpenseDatabase()

    # Create several expenses
    expense1 = Expense("Lunch", 12.50)
    expense2 = Expense("Coffee", 3.75)
    expense3 = Expense("Lunch", 15.00)

    # Add expenses to the database with error handling
    try:
        db.add_expense(expense1)
        db.add_expense(expense2)
        db.add_expense(expense3)
    except TypeError as e:
        print("Error adding expense:", e)

    print("Initial expenses:")
    for expense in db.to_dict():
        print(expense)

    # Update expense1 and display
    expense1.update(amount=13.00)
    print("\nAfter updating expense1:")
    print(expense1.to_dict())

    # Retrieve expense by its ID (using expense2's id)
    retrieved = db.get_expense_by_id(expense2.id)
    print("\nRetrieved expense by ID:")
    if retrieved:
        print(retrieved.to_dict())
    else:
        print("Expense not found.")

    # Retrieve expenses by title "Lunch" with error handling
    try:
        lunches = db.get_expense_by_title("Lunch")
        print("\nExpenses with title 'Lunch':")
        for expense in lunches:
            print(expense.to_dict())
    except ValueError as ve:
        print("Error retrieving expenses by title:", ve)

    # Remove expense2 from the database and check removal status
    removed = db.remove_expense(expense2.id)
    if removed:
        print("\nExpense removed successfully.")
    else:
        print("\nNo expense found with the given ID to remove.")

    print("\nAfter removing expense2:")
    for expense in db.to_dict():
        print(expense)