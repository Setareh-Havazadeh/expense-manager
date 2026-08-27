class ExpenseManager:
    def __init__(self):
        self.expense = []

    def addExpense(self):
        title = input("Please enter the title: ")
        amount = int(input("Please enter the amount: "))
        category = input("Please enter the category: ")

        self.expense.append({"title": title, "amount": amount, "category": category})

    def showExpenses(self):
        pass

    def searchExpenses(self):
        pass

    def deleteExpense(self):
        pass

    def totalExpenses(self):
        pass

    def statistics(self):
        pass
