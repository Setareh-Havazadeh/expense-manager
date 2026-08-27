class ExpenseManager:
    def __init__(self):
        self.expense = []

    def addExpense(self, title, amount, category):

        self.expense.append({"title": title, "amount": amount, "category": category})

    def showExpenses(self):
        for i in self.expense:
            for key, value in i.items():
                print(f"{key}: {value}")

    def searchExpenses(self):
        pass

    def deleteExpense(self):
        pass

    def totalExpenses(self):
        pass

    def statistics(self):
        pass
