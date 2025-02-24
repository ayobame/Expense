# Expense Tracker
 The purpose of this project is to implement two classes, Expense and ExpenseDatabase, to model and manage financial expenses. The Python script provides a simple expense tracking system. It includes two main classes: `Expense` and `ExpenseDatabase`. The `Expense` class represents an individual expense, while the `ExpenseDatabase` class manages a collection of expenses.

 ---

## Features
- **Expense Management:** Create, update, and track expenses with a title, amount, and timestamps.
- **Expense Database:** Store and manage multiple expenses in a database-like structure.
- **Search and Filter:** Retrieve expenses by ID or title.
- **Data Serialization:** Convert expenses to dictionary format for easy storage or transmission.
- **Error Handling:** Robust validation for inputs (e.g., empty titles, negative amounts).


---

## Usage

### Expense Class
The `Expense` class represents an individual expense. It includes the following methods:

#### `__init__(title: str, amount: float)`
- Initializes a new expense with a title, amount, and auto-generated timestamps.
- **Raises**:
  - `ValueError`: If the title is empty or the amount is negative.

#### `update(title: Optional[str] = None, amount: Optional[float] = None)`
- Updates the expense's title or amount. Only non-`None` values are updated.
- **Raises**:
  - `ValueError`: If the title is empty or the amount is negative.

#### `to_dict() -> dict`
- Returns a dictionary representation of the expense, including timestamps in ISO 8601 format.

---

### ExpenseDatabase Class
The `ExpenseDatabase` class manages a collection of expenses. It includes the following methods:

#### `__init__()`
- Initializes an empty list to store expenses.

#### `add_expense(expense: Expense)`
- Adds an expense to the database.
- **Raises**:
  - `TypeError`: If the input is not an instance of `Expense`.

#### `remove_expense(expense_id: str) -> bool`
- Removes an expense by its unique ID.
- **Returns**:
  - `True` if the expense was removed, `False` otherwise.

#### `get_expense_by_id(expense_id: str) -> Optional[Expense]`
- Retrieves an expense by its unique ID.
- **Returns**:
  - The matching `Expense` object, or `None` if not found.

#### `get_expense_by_title(title: str) -> List[Expense]`
- Retrieves all expenses with a matching title.
- **Raises**:
  - `ValueError`: If the title is an empty string.
- **Returns**:
  - A list of `Expense` objects with the given title.

#### `to_dict() -> List[dict]`
- Returns a list of dictionary representations of all expenses in the database.

---

## Example
```python
# Create an instance of ExpenseDatabase
db = ExpenseDatabase()

# Create expenses
expense1 = Expense("Lunch", 12.50)
expense2 = Expense("Coffee", 3.75)
expense3 = Expense("Lunch", 15.00)

# Add expenses to the database
db.add_expense(expense1)
db.add_expense(expense2)
db.add_expense(expense3)

# Update an expense
expense1.update(amount=13.00)

# Retrieve an expense by ID
retrieved = db.get_expense_by_id(expense2.id)
if retrieved:
    print(retrieved.to_dict())

# Retrieve expenses by title
lunches = db.get_expense_by_title("Lunch")
for expense in lunches:
    print(expense.to_dict())

# Remove an expense
removed = db.remove_expense(expense2.id)
if removed:
    print("Expense removed successfully.")

# Print all expenses
for expense in db.to_dict():
    print(expense)
```

---

## Error Handling
The code includes robust error handling for:
- Empty titles.
- Negative amounts.
- Invalid expense objects.
- Invalid amount formats.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
