from re import search

from expense_manager import ExpenseManager
from input_handler import InputHandler


class MenuHandler:
    def __init__(self):
        self.expense_manager = ExpenseManager()

        self.input_handler = InputHandler()

    def format_expense(self, expense):
        return f"title: {expense['title']}, amount: {expense['amount']}, category: {expense['category']}, date: {expense['date']}"

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
                    expenses = self.expense_manager.show_expenses()
                    for expense in expenses:
                        print(self.format_expense(expense))

                elif menu_choice == 3:

                    print("Please enter the search term: ")
                    search_choice = self.input_handler.text_input()
                    result = self.expense_manager.search_expenses(search_choice)
                    for expense in result:
                        print(self.format_expense(expense))

                elif menu_choice == 4:
                    print("To edit an expense, please enter the title:")
                    edit_choice = self.input_handler.text_input()
                    search_result = self.expense_manager.find_expenses(edit_choice)

                    match_count = 0
                    for expense in search_result:
                        match_count += 1
                        print(f"{match_count}.{self.format_expense(expense)}")
                    if search_result:
                        print(
                            "Please enter the number of the expense you want to edit from the list above: "
                        )
                        user_choice = self.input_handler.numeric_input()

                        if user_choice > 0 and user_choice <= len(search_result):

                            print("Please enter the new title:")
                            new_title = self.input_handler.text_input()
                            print("Please enter the new amount:")
                            new_amount = self.input_handler.numeric_input()
                            print("Please enter the new category:")
                            new_category = self.input_handler.text_input()
                            self.expense_manager.edit_expense(
                                search_result[user_choice - 1],
                                new_title,
                                new_amount,
                                new_category,
                            )
                            print("Successfully updated the list.")

                        else:
                            print(
                                "invalid selection. Please enter a number from the list."
                            )

                    else:
                        print("list is empty. Please add an expense first.")

                elif menu_choice == 5:
                    print("Please enter the title of the expense you want to delete:")
                    delete_choice = self.input_handler.text_input()
                    search_result = self.expense_manager.find_expenses(delete_choice)
                    match_count = 0
                    for expense in search_result:
                        match_count += 1
                        print(f"{match_count}.{self.format_expense(expense)}")
                    print(
                        "Please enter the number of the expense you want to delete from the list above: "
                    )
                    user_choice = self.input_handler.numeric_input()
                    if user_choice > 0 and user_choice <= len(search_result):
                        self.expense_manager.delete_expense(
                            search_result[user_choice - 1]
                        )
                        print("Successfully deleted the expense from the list.")
                    else:
                        print("Invalid selection. Please enter a number from the list.")

                elif menu_choice == 6:
                    print(f"Your total costs: {self.expense_manager.total_expenses()}")

                elif menu_choice == 7:
                    if self.expense_manager.expenses:
                        expense_statistic, category_statistics = (
                            self.expense_manager.statistics()
                        )
                        for key, value in expense_statistic.items():
                            print(f"{key}: {value}")
                        print("============ Category Statistics ============")
                        for category in category_statistics:
                            print(
                                f"Category Name: {category['category']}, \t \nNumber of expenses in this category: {category['count']}, \t \nTotal costs: {category['costs']} \n"
                            )
                    else:
                        print(
                            "You haven't entered any expenses, and your management list is empty!"
                        )

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
