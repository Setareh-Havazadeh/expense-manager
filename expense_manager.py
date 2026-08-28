class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def get_expense_amounts(self):
        expense_amounts = []
        for expense in self.expenses:
            expense_amounts.append(expense["amount"])

        return expense_amounts

    def addExpense(self, title, amount, category):

        self.expenses.append({"title": title, "amount": amount, "category": category})

    def showExpenses(self):
        for expense in self.expenses:
                print(f"title: {expense['title']}, amount: {expense['amount']}, category: {expense['category']}")

    def searchExpenses(self, search):
        search_found = False
        for expense in self.expenses:
            if search == expense["title"] or search == expense["category"]:
                print(f"title: {expense['title']}, amount: {expense['amount']}, category: {expense['category']}")
                search_found = True
        if not search_found:
            print("The specified cost was not found in the list!!")

    def deleteExpense(self, del_title):
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

    def totalExpenses(self):

        expense_amounts = self.get_expense_amounts()
        return sum(expense_amounts)

    def statistics(self):
        if self.expenses:
            print(f"Number of your expenses: {len(self.expenses)}")
            print(f"Your total costs: {self.totalExpenses()}")

            expense_amounts = self.get_expense_amounts()


            print(f"Your highest expense: {max(expense_amounts)}")
        else:
            print("You haven't entered any expenses, and your management list is empty!")

