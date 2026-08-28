from expense_manager import ExpenseManager

expense_manager = ExpenseManager()


def main():
    while True:

        print("========== Expense Manager ==========")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Search Expenses")
        print("4. Delete Expense")
        print("5. Total Expenses")
        print("6. Statistics")
        print("7. Exit")

        value = int(
            input("What would you like to do? Please enter the desired number: ")
        )

        if value == 1:

            number = int(
                input("How many do you intend to import? Enter the desired number: ")
            )
            for i in range(number):
                title = input("Please enter the title: ")
                amount = int(input("Please enter the amount: "))
                category = input("Please enter the category: ")

                expense_manager.addExpense(title, amount, category)

        elif value == 2:
            expense_manager.showExpenses()

        elif value == 3:
            search = input("Please enter the search term: ")
            expense_manager.searchExpenses(search)

        elif value == 4:
            choos = input("To remove from the list, please enter the comment title:")
            expense_manager.deleteExpense(choos)

        elif value == 5:
            print(f"Your total costs: {expense_manager.totalExpenses()}")

        elif value == 6:
            expense_manager.statistics()
            
        elif value == 7:
            break


if __name__ == "__main__":
    main()
