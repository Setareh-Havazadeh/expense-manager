from expense_manager import ExpenseManager
from input_handler import InputHandler

expense_manager = ExpenseManager()

inputHandler = InputHandler()

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
        print("Enter the desired number from the list above.\nPlease ensure the selected number is within the range of the list (1–7).")
        
        menu_choice = inputHandler.numeric_input()
        
        if 1 <= menu_choice <= 7:
        
            if menu_choice == 1:
                expenses = inputHandler.get_expenses()
                for expense in expenses:
                    expense_manager.addExpense(expense["title"], expense["amount"], expense["category"])

            elif menu_choice == 2:
                expense_manager.showExpenses()

            elif menu_choice == 3:
                
                print("Please enter the search term: ")
                search_choice = inputHandler.text_input()
                expense_manager.searchExpenses(search_choice)

            elif menu_choice == 4:
                print("To remove from the list, please enter the comment title:")
                remove_choice = inputHandler.text_input()
                expense_manager.deleteExpense(remove_choice)

            elif menu_choice == 5:
                print(f"Your total costs: {expense_manager.totalExpenses()}")

            elif menu_choice == 6:
                expense_manager.statistics()
                
            elif menu_choice == 7:
                print("Are you sure you want to exit?(Y/N)")
                exit_choice = inputHandler.text_input()
                if exit_choice == "Y":
                    print("You have logged out.")
                    break
                elif exit_choice == "N":
                    continue
        else:
            print("Please select from the specified range (1 to 7).try agin!!")
            continue



if __name__ == "__main__":
    main()
