from datetime import date
import json
import os
from input_handler import InputHandler


class ExpenseManager:
    def __init__(self):

        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []

        self.budget = 0
        self.input_handler = InputHandler()

    def format_expense(self, expense):

        return f"title: {expense['title']}, amount: {expense['amount']}, category: {expense['category']}, date: {expense['date']}"

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
        if self.expenses:

            for expense in self.expenses:
                print(self.format_expense(expense))

    def search_expenses(self, search):
        result = self.find_expenses(search)
        if result:
            for expense in result:
                print(self.format_expense(expense))

        else:
            print("Your list is empty.")

    def edit_expense(self, title, new_title, new_amount, new_category):
        expense_found = False
        for expense in self.expenses:
            if title == expense["title"]:
                expense["title"] = new_title
                expense["amount"] = new_amount
                expense["category"] = new_category
                expense_found = True
                print("Successfully updated the list.")
                self.save_expenses()
                break

        if not expense_found:
            print("The specified cost was not found in the list!!")

    def delete_expense(self, search_title):
        match_count = 0
        result = self.find_expenses(search_title)
        if result:
            for expense in result:
                match_count += 1
                print(f"{match_count}.{self.format_expense(expense)}")

            user_choice = self.input_handler.numeric_input()
            if user_choice > 0 and user_choice <= len(result):
                self.expenses.remove(result[user_choice - 1])
                print("Expense deleted successfully.")
                self.save_expenses()
            else:
                print("Invalid selection. Please enter a number from the list.")
        else:
            print("Your list is empty.")

    def total_expenses(self):

        expense_amounts = self.get_expense_amounts()
        return sum(expense_amounts)

    def statistics(self):
        if self.expenses:

            print(f"Number of your expenses: {len(self.expenses)}")

            expense_amounts = self.get_expense_amounts()

            print(f"Your total costs: {sum(expense_amounts)}")

            print(f"Your highest expense: {max(expense_amounts)}")

            print(f"Your lowest cost: {min(expense_amounts)}")

            print(f"Your average costs: {sum(expense_amounts)/len(expense_amounts)}")

            print("============ Category Statistics ============")
            category_statistics = self.category_summary()
            for category in category_statistics:
                print(
                    f"Category Name: {category['category']}, \t \nNumber of expenses in this category: {category['count']}, \t \nTotal costs: {category['costs']} \n"
                )
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
