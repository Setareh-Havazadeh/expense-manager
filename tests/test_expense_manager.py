from expense_manager import ExpenseManager


def test_total_expenses():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        },
        {
            "title": "Expense 2",
            "amount": 20,
            "category": "Category 2",
            "date": "2023-01-02",
        },
        {
            "title": "Expense 3",
            "amount": 30,
            "category": "Category 1",
            "date": "2023-01-03",
        },
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
        {
            "title": "Expense 1",
            "amount": -10,
            "category": "Category 1",
            "date": "2023-01-01",
        },
        {
            "title": "Expense 2",
            "amount": -20,
            "category": "Category 2",
            "date": "2023-01-02",
        },
    ]

    total = expense_manager.total_expenses()

    assert total == -30


def test_total_expenses_mixed():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        },
        {
            "title": "Expense 2",
            "amount": -20,
            "category": "Category 2",
            "date": "2023-01-02",
        },
        {
            "title": "Expense 3",
            "amount": 30,
            "category": "Category 1",
            "date": "2023-01-03",
        },
    ]

    total = expense_manager.total_expenses()

    assert total == 20


def test_find_expenses():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        },
        {
            "title": "Expense 2",
            "amount": 20,
            "category": "Category 2",
            "date": "2023-01-02",
        },
        {
            "title": "Expense 3",
            "amount": 30,
            "category": "Category 1",
            "date": "2023-01-03",
        },
    ]

    results = expense_manager.find_expenses("Expense")

    assert len(results) == 3


def test_find_expenses_no_results():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        },
        {
            "title": "Expense 2",
            "amount": 20,
            "category": "Category 2",
            "date": "2023-01-02",
        },
    ]

    results = expense_manager.find_expenses("Nonexistent")

    assert len(results) == 0


def test_find_expenses_case_insensitive():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        },
        {
            "title": "Expense 2",
            "amount": 20,
            "category": "Category 2",
            "date": "2023-01-02",
        },
    ]

    results = expense_manager.find_expenses("expense")

    assert len(results) == 2


def test_find_expenses_partial_match():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        },
        {
            "title": "Expense 2",
            "amount": 20,
            "category": "Category 2",
            "date": "2023-01-02",
        },
        {
            "title": "Another Expense",
            "amount": 30,
            "category": "Category 1",
            "date": "2023-01-03",
        },
    ]

    results = expense_manager.find_expenses("Another")

    assert len(results) == 1


def test_find_expenses_empty_search():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        },
        {
            "title": "Expense 2",
            "amount": 20,
            "category": "Category 2",
            "date": "2023-01-02",
        },
    ]

    results = expense_manager.find_expenses("")

    assert len(results) == 0


def test_category_summary():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        },
        {
            "title": "Expense 2",
            "amount": 20,
            "category": "Category 2",
            "date": "2023-01-02",
        },
        {
            "title": "Expense 3",
            "amount": 30,
            "category": "Category 1",
            "date": "2023-01-03",
        },
    ]

    summary = expense_manager.category_summary()

    assert len(summary) == 2
    assert summary[0]["category"] == "Category 1"
    assert summary[0]["count"] == 2
    assert summary[0]["costs"] == 40
    assert summary[1]["category"] == "Category 2"
    assert summary[1]["count"] == 1
    assert summary[1]["costs"] == 20


def test_category_summary_empty():
    expense_manager = ExpenseManager()
    expense_manager.expenses = []

    summary = expense_manager.category_summary()

    assert len(summary) == 0


def test_category_summary_single_category():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        },
        {
            "title": "Expense 2",
            "amount": 20,
            "category": "Category 1",
            "date": "2023-01-02",
        },
        {
            "title": "Expense 3",
            "amount": 30,
            "category": "Category 1",
            "date": "2023-01-03",
        },
    ]

    summary = expense_manager.category_summary()

    assert len(summary) == 1
    assert summary[0]["category"] == "Category 1"
    assert summary[0]["count"] == 3
    assert summary[0]["costs"] == 60


def test_category_summary_multiple_categories():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        },
        {
            "title": "Expense 2",
            "amount": 20,
            "category": "Category 2",
            "date": "2023-01-02",
        },
        {
            "title": "Expense 3",
            "amount": 30,
            "category": "Category 3",
            "date": "2023-01-03",
        },
    ]

    summary = expense_manager.category_summary()

    assert len(summary) == 3
    assert summary[0]["category"] == "Category 1"
    assert summary[0]["count"] == 1
    assert summary[0]["costs"] == 10
    assert summary[1]["category"] == "Category 2"
    assert summary[1]["count"] == 1
    assert summary[1]["costs"] == 20
    assert summary[2]["category"] == "Category 3"
    assert summary[2]["count"] == 1
    assert summary[2]["costs"] == 30


def test_add_expense():
    expense_manager = ExpenseManager()
    expense_manager.expenses = []

    expense_manager.add_expense("Expense 1", 10, "Category 1")

    assert len(expense_manager.expenses) == 1
    assert expense_manager.expenses[0]["title"] == "Expense 1"
    assert expense_manager.expenses[0]["amount"] == 10
    assert expense_manager.expenses[0]["category"] == "Category 1"


def test_add_expense_multiple():
    expense_manager = ExpenseManager()
    expense_manager.expenses = []

    expense_manager.add_expense("Expense 1", 10, "Category 1")
    expense_manager.add_expense("Expense 2", 20, "Category 2")

    assert len(expense_manager.expenses) == 2
    assert expense_manager.expenses[0]["title"] == "Expense 1"
    assert expense_manager.expenses[0]["amount"] == 10
    assert expense_manager.expenses[0]["category"] == "Category 1"
    assert expense_manager.expenses[1]["title"] == "Expense 2"
    assert expense_manager.expenses[1]["amount"] == 20
    assert expense_manager.expenses[1]["category"] == "Category 2"


def test_add_expense_negative_amount():
    expense_manager = ExpenseManager()
    expense_manager.expenses = []

    expense_manager.add_expense("Expense 1", -10, "Category 1")

    assert len(expense_manager.expenses) == 1
    assert expense_manager.expenses[0]["title"] == "Expense 1"
    assert expense_manager.expenses[0]["amount"] == -10
    assert expense_manager.expenses[0]["category"] == "Category 1"


def test_add_expense_save():
    expense_manager = ExpenseManager()
    expense_manager.expenses = []

    expense_manager.add_expense("Expense 1", 10, "Category 1")

    with open("expenses.json", "r", encoding="utf-8") as file:
        data = file.read()

    assert '"title": "Expense 1"' in data
    assert '"amount": 10' in data
    assert '"category": "Category 1"' in data
