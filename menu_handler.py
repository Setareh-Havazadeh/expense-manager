from expense_manager import ExpenseManager
from input_handler import InputHandler


class MenuHandler:
    def __init__(self):
        self.expense_manager = ExpenseManager()

        self.input_handler = InputHandler()

    def show_menu(self):
        print("========== Expense Manager ==========")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Search Expenses")
        print("4. Edit Expense")
        print("5. Delete Expense")
        print("6. Total Expenses")
        print("7. Statistics")
        print("8. Set Budget")
        print("9. Budget Status")
        print("10. Exit")
        print(
            "Enter the desired number from the list above.\nPlease ensure the selected number is within the range of the list (1–10)."
        )
        menu_choice = self.input_handler.numeric_input()
        return menu_choice

    def menu(self):

        while True:
            menu_choice = self.show_menu()
            if 1 <= menu_choice <= 10:

                if menu_choice == 1:
                    expenses = self.input_handler.get_expenses()
                    for expense in expenses:
                        self.expense_manager.add_expense(
                            expense["title"], expense["amount"], expense["category"]
                        )

                elif menu_choice == 2:
                    self.expense_manager.show_expenses()

                elif menu_choice == 3:

                    print("Please enter the search term: ")
                    search_choice = self.input_handler.text_input()
                    self.expense_manager.search_expenses(search_choice)

                elif menu_choice == 4:
                    print("To edit an expense, please enter the title:")
                    edit_choice = self.input_handler.text_input()
                    print("Please enter the new title:")
                    new_title = self.input_handler.text_input()
                    print("Please enter the new amount:")
                    new_amount = self.input_handler.numeric_input()
                    print("Please enter the new category:")
                    new_category = self.input_handler.text_input()
                    self.expense_manager.edite_expense(edit_choice, new_title, new_amount, new_category)

                elif menu_choice == 5:
                    print("Please enter the title of the expense you want to delete:")
                    delete_choice = self.input_handler.text_input()
                    self.expense_manager.delete_expense(delete_choice)

                elif menu_choice == 6:
                    print(f"Your total costs: {self.expense_manager.total_expenses()}")

                elif menu_choice == 7:
                    self.expense_manager.statistics()

                elif menu_choice == 8:
                    print("Please enter the total budget: ")
                    budget = self.input_handler.numeric_input()
                    self.expense_manager.set_budget(budget)

                elif menu_choice == 9:
                    self.expense_manager.show_budget()

                elif menu_choice == 10:
                    print("Are you sure you want to exit?(Y/N)")
                    exit_choice = self.input_handler.text_input()
                    if exit_choice == "Y":
                        print("You have logged out.")
                        break
                    elif exit_choice == "N":
                        continue
            else:
                print("Please select from the specified range (1 to 10).try agin!!")
                continue
