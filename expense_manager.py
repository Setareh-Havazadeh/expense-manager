from datetime import date
import json
import os


class ExpenseManager:
    def __init__(self):

        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []

        self.budget = 0

    def find_expenses(self, find):
        results = []
        find_lower = find.lower()
        if self.expenses:
            for expense in self.expenses:
                if (
                    find_lower in expense["title"].lower()
                    or find_lower in expense["category"].lower()
                ):
                    results.append(expense)
        else:
            print(
                "You haven't entered any expenses, and your management list is empty!"
            )

        return results

    def get_expense_amounts(self):
        return [expense["amount"] for expense in self.expenses]

    def category_summary(self):

        category_totals = {}
        for expense in self.expenses:
            category = expense["category"]
            if category in category_totals:
                category_totals[category]["count"] += 1
                category_totals[category]["costs"] += expense["amount"]
            else:
                category_totals[category] = {
                    "category": category,
                    "count": 1,
                    "costs": expense["amount"],
                }

        return list(category_totals.values())

    def save_expenses(self):
        with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(self.expenses, file, ensure_ascii=False, indent=4)

    def add_expense(self, title, amount, category):
        add_date = date.today().isoformat()
        self.expenses.append(
            {"title": title, "amount": amount, "category": category, "date": add_date}
        )

        self.save_expenses()

    def show_expenses(self):
        return self.expenses

    def edit_expense(self, expense, new_title, new_amount, new_category):

        if expense in self.expenses:
            expense["title"] = new_title
            expense["amount"] = new_amount
            expense["category"] = new_category
            self.save_expenses()

    def delete_expense(self, expense):
        if expense in self.expenses:
            self.expenses.remove(expense)
            self.save_expenses()

    def total_expenses(self):

        expense_amounts = self.get_expense_amounts()
        return sum(expense_amounts)

    def statistics(self):
        expense_statistic = {}
        number = len(self.expenses)

        expense_amounts = self.get_expense_amounts()

        total_costs = sum(expense_amounts)

        max_cost = max(expense_amounts)

        min_cost = min(expense_amounts)

        average_cost = sum(expense_amounts) / len(expense_amounts)

        expense_statistic["Total Expenses"] = total_costs
        expense_statistic["Number of Expenses"] = number
        expense_statistic["Maximum Expense"] = max_cost
        expense_statistic["Minimum Expense"] = min_cost
        expense_statistic["Average Expense"] = average_cost

        category_statistics = self.category_summary()
        return expense_statistic, category_statistics

    def set_budget(self, budget):
        self.budget = budget
