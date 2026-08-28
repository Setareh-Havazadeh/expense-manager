class ExpenseManager:
    def __init__(self):
        self.expense = []

    def addExpense(self, title, amount, category):

        self.expense.append({"title": title, "amount": amount, "category": category})

    def showExpenses(self):
        for i in self.expense:
            for key, value in i.items():
                print(f"{key}: {value}")

    def searchExpenses(self, search):
        found = False
        for i in self.expense:
            for key, value in i.items():
                if search == value and (key == "title" or key == "category"):
                    print(f"{key}: {value}")
                    found = True

        if found == False:
            print("The specified cost was not found in the list!!")

    def deleteExpense(self, del_title):
        found = False
        for i in self.expense:
            if del_title == i["title"]:
                self.expense.remove(i)
                found = True
                print("Successfully removed from the list.")
            if found == True:
                break

        if found == False:
            print("The specified cost was not found in the list!!")

    def totalExpenses(self):
        total = 0
        for i in self.expense:
            total = total + i["amount"]

        return total

    def statistics(self):
        if len(self.expense) > 0:
            print(f"Number of your expenses: {len(self.expense)}")
            print(f"Your total costs: {self.totalExpenses()}")

            maximum = 0
            for i in self.expense:
                if maximum < i["amount"]:
                    maximum = i["amount"]

            print(f"Your highest expense: {maximum}")
        else:
            print("You haven't entered any expenses, and your management list is empty!")

