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

    def get_expense_amounts(self):
        expense_amounts = []
        for expense in self.expenses:
            expense_amounts.append(expense["amount"])

        return expense_amounts

    def category_summary(self):

        total_categories = []
        for categories in self.expenses:
            found = False
            if total_categories:
                for categorys in total_categories:
                    if categorys["category"] == categories["category"]:
                        categorys["count"] += 1
                        categorys["costs"] += categories["amount"]
                        found = True
                if found == False:
                    total_categories.append(
                        {
                            "category": categories["category"],
                            "count": 1,
                            "costs": categories["amount"],
                        }
                    )
            else:
                total_categories.append(
                    {
                        "category": categories["category"],
                        "count": 1,
                        "costs": categories["amount"],
                    }
                )

        return total_categories

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
                print(
                    f"title: {expense['title']}, amount: {expense['amount']}, category: {expense['category']}, date: {expense['date']}"
                )

    def search_expenses(self, search):
        search_found = False
        for expense in self.expenses:
            if search == expense["title"] or search == expense["category"]:
                print(
                    f"title: {expense['title']}, amount: {expense['amount']}, category: {expense['category']}, date: {expense['date']}"
                )
                search_found = True
        if not search_found:
            print("The specified cost was not found in the list!!")

    def edite_expense(self, edite_title, new_title, new_amount, new_category):
        expense_found = False
        for expense in self.expenses:
            if edite_title == expense["title"]:
                expense["title"] = new_title
                expense["amount"] = new_amount
                expense["category"] = new_category
                expense_found = True
                print("Successfully updated the list.")
                self.save_expenses()
                break

        if not expense_found:
            print("The specified cost was not found in the list!!")

    def delete_expense(self, del_title):
        expense_found = False
        for expense in self.expenses:
            if del_title == expense["title"]:
                self.expenses.remove(expense)
                expense_found = True
                print("Successfully removed from the list.")
                self.save_expenses()
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
