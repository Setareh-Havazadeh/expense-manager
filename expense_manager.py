from datetime import date
from itertools import count
from unicodedata import category


class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.budget = 0

    def get_expense_amounts(self):
        expense_amounts = []
        for expense in self.expenses:
            expense_amounts.append(expense["amount"])

        return expense_amounts

    def add_expense(self, title, amount, category):
        add_date = date.today()
        self.expenses.append(
            {"title": title, "amount": amount, "category": category, "date": add_date}
        )

    def show_expenses(self):
        categorys = []
        for expenses in self.expenses:
            print(
                f"title: {expenses['title']}, amount: {expenses['amount']}, category: {expenses['category']}, date: {expenses['date']}"
            )
            categorys.append(
                {"category": expenses["category"], "amount": expenses["amount"]}
            )
        print("========================================================")
        total_categories = []
        for category in categorys:
            found = False
            if total_categories:
                for categoyies in total_categories:
                    if categoyies["category"] == category["category"]:
                        categoyies["count"] += 1
                        categoyies["costs"] += category["amount"]
                        found = True
                if found == False:
                    total_categories.append(
                        {
                            "category": category["category"],
                            "count": 1,
                            "costs": category["amount"],
                        }
                    )
            else:
                total_categories.append(
                    {
                        "category": category["category"],
                        "count": 1,
                        "costs": category["amount"],
                    }
                )

        for categories in total_categories:
            print(
                f"Category Name: {categories['category']}, Number of expenses in this category: {categories['count']}, Total costs: {categories['costs']}"
            )

    def searche_xpenses(self, search):
        search_found = False
        for expense in self.expenses:
            if search == expense["title"] or search == expense["category"]:
                print(
                    f"title: {expense['title']}, amount: {expense['amount']}, category: {expense['category']}, date: {expense['date']}"
                )
                search_found = True
        if not search_found:
            print("The specified cost was not found in the list!!")

    def delete_expense(self, del_title):
        expense_found = False
        for expense in self.expenses:
            if del_title == expense["title"]:
                self.expenses.remove(expense)
                expense_found = True
                print("Successfully removed from the list.")
            if expense_found:
                break

        if not expense_found:
            print("The specified cost was not found in the list!!")

    def total_expenses(self):

        expense_amounts = self.get_expense_amounts()
        return sum(expense_amounts)

    def statistics(self):
        if self.expenses:
            print(f"Number of your expenses: {len(self.expenses)}")
            print(f"Your total costs: {self.total_expenses()}")

            expense_amounts = self.get_expense_amounts()

            print(f"Your highest expense: {max(expense_amounts)}")
        else:
            print(
                "You haven't entered any expenses, and your management list is empty!"
            )

    def set_budget(self, budget):
        self.budget = budget

    def show_budget(self):
        total = self.total_expenses()
        remaining = self.budget - total
        if self.budget:
            print(
                f"Budget: {self.budget}, Total Expenses: {total}, Remaining Budget: {remaining}"
            )
        else:
            print("Your total budget is empty; please enter an amount and try again.")
