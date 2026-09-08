import json

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
    assert [expense["title"] for expense in results] == [
        "Expense 1",
        "Expense 2",
        "Expense 3",
    ]


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

    assert results == []


def test_find_expenses_by_category():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Food",
            "date": "2023-01-01",
        }
    ]

    results = expense_manager.find_expenses("food")

    assert results == [expense_manager.expenses[0]]


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

    assert [expense["title"] for expense in results] == [
        "Expense 1",
        "Expense 2",
    ]


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

    assert results[0]["title"] == "Another Expense"


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

    assert [expense["title"] for expense in results] == [
        "Expense 1",
        "Expense 2",
    ]


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


def test_add_expense():
    expense_manager = ExpenseManager()
    expense_manager.expenses = []

    expense_manager.add_expense("Expense 1", 10, "Category 1")

    assert len(expense_manager.expenses) == 1
    assert expense_manager.expenses[0]["title"] == "Expense 1"
    assert expense_manager.expenses[0]["amount"] == 10
    assert expense_manager.expenses[0]["category"] == "Category 1"
    assert "date" in expense_manager.expenses[0]


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


def test_add_expense_save(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    expense_manager = ExpenseManager()
    expense_manager.expenses = []

    expense_manager.add_expense("Expense 1", 10, "Category 1")

    with open("expenses.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data == expense_manager.expenses


def test_edit_expense():
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

    expense_manager.edit_expense(
        expense_manager.expenses[0],
        "Expense 5",
        40,
        "Category 5",
    )
    assert expense_manager.expenses[0]["title"] == "Expense 5"
    assert expense_manager.expenses[0]["amount"] == 40
    assert expense_manager.expenses[0]["category"] == "Category 5"
    assert expense_manager.expenses[0]["date"] == "2023-01-01"
    assert expense_manager.expenses[1]["title"] == "Expense 2"
    assert expense_manager.expenses[1]["amount"] == 20
    assert expense_manager.expenses[1]["category"] == "Category 1"
    assert expense_manager.expenses[1]["date"] == "2023-01-02"


def test_edit_expense_invalid_expense():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        }
    ]

    invalid_expense = {
        "title": "Invalid Expense",
        "amount": 20,
        "category": "Category 2",
        "date": "2023-01-02",
    }

    expense_manager.edit_expense(
        invalid_expense,
        "Expense 5",
        40,
        "Category 5",
    )

    assert expense_manager.expenses[0]["title"] == "Expense 1"
    assert expense_manager.expenses[0]["amount"] == 10
    assert expense_manager.expenses[0]["category"] == "Category 1"


def test_edit_expense_save(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        }
    ]

    expense_manager.edit_expense(
        expense_manager.expenses[0],
        "Expense 5",
        40,
        "Category 5",
    )

    with open("expenses.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data == expense_manager.expenses


def test_delete_expense():
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

    expense_manager.delete_expense(expense_manager.expenses[0])

    assert len(expense_manager.expenses) == 1
    assert expense_manager.expenses[0]["title"] == "Expense 2"


def test_delete_expense_invalid():
    expense_manager = ExpenseManager()
    expense_manager.expenses = [
        {
            "title": "Expense 1",
            "amount": 10,
            "category": "Category 1",
            "date": "2023-01-01",
        }
    ]

    invalid_expense = {
        "title": "Invalid Expense",
        "amount": 20,
        "category": "Category 2",
        "date": "2023-01-02",
    }

    expense_manager.delete_expense(invalid_expense)

    assert len(expense_manager.expenses) == 1
    assert expense_manager.expenses[0]["title"] == "Expense 1"


def test_delete_expense_save(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
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

    expense_manager.delete_expense(expense_manager.expenses[0])

    with open("expenses.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data == expense_manager.expenses


def test_set_budget():
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
    expense_manager.set_budget(100)

    assert expense_manager.budget == 100


def test_set_negative_budget():
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
    expense_manager.set_budget(-50)

    assert expense_manager.budget == -50


def test_statistics_expenses():
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

    expense_statistic, category_statistics = expense_manager.statistics()

    assert expense_statistic["Total Expenses"] == 60
    assert expense_statistic["Number of Expenses"] == 3
    assert expense_statistic["Maximum Expense"] == 30
    assert expense_statistic["Minimum Expense"] == 10
    assert expense_statistic["Average Expense"] == 20.0

    assert len(category_statistics) == 2


def test_statistics_expenses_empty():
    expense_manager = ExpenseManager()
    expense_manager.expenses = []

    expense_statistic, category_statistics = expense_manager.statistics()

    assert expense_statistic["Total Expenses"] == 0
    assert expense_statistic["Number of Expenses"] == 0
    assert expense_statistic["Maximum Expense"] is None
    assert expense_statistic["Minimum Expense"] is None
    assert expense_statistic["Average Expense"] is None
    assert category_statistics == []


def test_statistics_expenses_category_summary():
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

    _, category_statistics = expense_manager.statistics()

    assert len(category_statistics) == 2
    assert category_statistics[0]["category"] == "Category 1"
    assert category_statistics[0]["count"] == 2
    assert category_statistics[0]["costs"] == 40
    assert category_statistics[1]["category"] == "Category 2"
    assert category_statistics[1]["count"] == 1
    assert category_statistics[1]["costs"] == 20
