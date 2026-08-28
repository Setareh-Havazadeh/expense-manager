from expense_manager import ExpenseManager

expense_manager = ExpenseManager()

def numeric_input():
    while True:
        try:
            user_input = int(input())
            if user_input > 0:
                break
            else:
                print("Please try again and enter a positive number!!")
        except ValueError:
            print("Try again!")
            continue

    return user_input

def text_input():

    while True:
        text = input()
        if not text.isdigit() and len(text.strip()) > 0:
            break

    return text

def get_expenses():

    print ("Enter the number of expenses you wish to add to the list as a numerical value.")
    expense_count = numeric_input()
    expenses = []
    for _ in range(expense_count):
    
        print("Please enter the title:")
        title = text_input()
        print("Please enter the amount: ")
        amount = numeric_input()
        print("Please enter the category: ")
        category = text_input()
        expenses.append({"title":title, "amount":amount, "category":category})
    return expenses

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
        
        menu_choice = numeric_input()
        
        if 1 <= menu_choice <= 7:
        
            if menu_choice == 1:
                expenses = get_expenses()
                for expense in expenses:
                    expense_manager.addExpense(expense["title"], expense["amount"], expense["category"])

            elif menu_choice == 2:
                expense_manager.showExpenses()

            elif menu_choice == 3:
                
                print("Please enter the search term: ")
                search_choice = text_input()
                expense_manager.searchExpenses(search_choice)

            elif menu_choice == 4:
                print("To remove from the list, please enter the comment title:")
                remove_choice = text_input()
                expense_manager.deleteExpense(remove_choice)

            elif menu_choice == 5:
                print(f"Your total costs: {expense_manager.totalExpenses()}")

            elif menu_choice == 6:
                expense_manager.statistics()
                
            elif menu_choice == 7:
                print("Are you sure you want to exit?(Y/N)")
                exit_choice = text_input()
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
