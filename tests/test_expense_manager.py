from expense_manager import ExpenseManager

def test_total_expenses():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {"title": "Expense 1", "amount": 10, "category": "Category 1", "date": "2023-01-01"},
        {"title": "Expense 2", "amount": 20, "category": "Category 2", "date": "2023-01-02"},
        {"title": "Expense 3", "amount": 30, "category": "Category 1", "date": "2023-01-03"},
    ]

    total = expense_manager.total_expenses()

    assert total == 60

def test_total_expenses_empty():
    expense_manager = ExpenseManager()
    expense_manager.expenses = []

    total = expense_manager.total_expenses()

    assert total == 0

def test_total_expenses_negative():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {"title": "Expense 1", "amount": -10, "category": "Category 1", "date": "2023-01-01"},
        {"title": "Expense 2", "amount": -20, "category": "Category 2", "date": "2023-01-02"},
    ]

    total = expense_manager.total_expenses()

    assert total == -30

def test_total_expenses_mixed():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {"title": "Expense 1", "amount": 10, "category": "Category 1", "date": "2023-01-01"},
        {"title": "Expense 2", "amount": -20, "category": "Category 2", "date": "2023-01-02"},
        {"title": "Expense 3", "amount": 30, "category": "Category 1", "date": "2023-01-03"},
    ]

    total = expense_manager.total_expenses()

    assert total == 20
