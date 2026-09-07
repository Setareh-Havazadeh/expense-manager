from expense_manager import ExpenseManager
from input_handler import InputHandler


class MenuHandler:
    def __init__(self):
        self.expense_manager = ExpenseManager()

        self.input_handler = InputHandler()

    def show_add_expense_menu(self):
        print(
            "Enter the number of expenses you wish to add to the list as a numerical value."
        )
        expense_count = self.input_handler.numeric_input()
        expenses = []
        for _ in range(expense_count):

            print("Please enter the title:")
            title = self.input_handler.text_input()
            print("Please enter the amount: ")
            amount = self.input_handler.numeric_input()
            print("Please enter the category: ")
            category = self.input_handler.text_input()
            expenses.append({"title": title, "amount": amount, "category": category})
        return expenses

    def show_list_of_expenses(self):
        expenses = self.expense_manager.show_expenses()
        for expense in expenses:
            print(self.format_expense(expense))

    def show_search_results(self, search_term):
        results = self.expense_manager.find_expenses(search_term)
        for expense in results:
            print(self.format_expense(expense))

    def select_expense(self, expenses, selection_prompt):
        for number, expense in enumerate(expenses, start=1):
            print(f"{number}.{self.format_expense(expense)}")

        if not expenses:
            return None

        print(selection_prompt)
        user_choice = self.input_handler.numeric_input()
        if 1 <= user_choice <= len(expenses):
            return expenses[user_choice - 1]

        return None

    def show_edit_expense_menu(self, expenses):
        selected_expense = self.select_expense(
            expenses,
            "Please enter the number of the expense you want to edit from the list above: ",
        )

        if selected_expense is None:
            if expenses:
                print("invalid selection. Please enter a number from the list.")
            else:
                print("list is empty. Please add an expense first.")
            return

        print("Please enter the new title:")
        new_title = self.input_handler.text_input()
        print("Please enter the new amount:")
        new_amount = self.input_handler.numeric_input()
        print("Please enter the new category:")
        new_category = self.input_handler.text_input()
        self.expense_manager.edit_expense(
            selected_expense,
            new_title,
            new_amount,
            new_category,
        )
        print("Successfully updated the list.")

    def show_delete_expense_menu(self, expenses):
        selected_expense = self.select_expense(
            expenses,
            "Please enter the number of the expense you want to delete from the list above: ",
        )

        if selected_expense is None:
            if expenses:
                print("Invalid selection. Please enter a number from the list.")
            else:
                print("List is empty. Please add an expense first.")
            return

        self.expense_manager.delete_expense(selected_expense)
        print("Successfully deleted the expense from the list.")

    def show_total_expenses(self):
        total_expenses = self.expense_manager.total_expenses()
        print(f"Total expenses: {total_expenses}")

    def show_statistics(self):
        if self.expense_manager.expenses:
            expense_statistic, category_statistics = self.expense_manager.statistics()
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

    def set_budget(self, budget):
        self.expense_manager.set_budget(budget)
        print(f"Budget set to: {budget}")

    def show_budget_status(self):
        total_expenses = self.expense_manager.total_expenses()
        budget = self.expense_manager.budget
        remaining_budget = budget - total_expenses
        print(
            f"Budget: {budget}, Total Expenses: {total_expenses}, Remaining Budget: {remaining_budget}"
        )

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
                    expenses = self.show_add_expense_menu()
                    for expense in expenses:
                        self.expense_manager.add_expense(
                            expense["title"], expense["amount"], expense["category"]
                        )

                elif menu_choice == 2:
                    self.show_list_of_expenses()

                elif menu_choice == 3:

                    print("Please enter the search term: ")
                    search_choice = self.input_handler.text_input()
                    self.show_search_results(search_choice)

                elif menu_choice == 4:
                    print("To edit an expense, please enter the title:")
                    edit_choice = self.input_handler.text_input()
                    search_result = self.expense_manager.find_expenses(edit_choice)

                    self.show_edit_expense_menu(search_result)

                elif menu_choice == 5:
                    print("Please enter the title of the expense you want to delete:")
                    delete_choice = self.input_handler.text_input()
                    search_result = self.expense_manager.find_expenses(delete_choice)
                    self.show_delete_expense_menu(search_result)

                elif menu_choice == 6:
                    self.show_total_expenses()

                elif menu_choice == 7:
                    self.show_statistics()

                elif menu_choice == 8:
                    print("Please enter the total budget: ")
                    budget = self.input_handler.numeric_input()
                    self.set_budget(budget)

                elif menu_choice == 9:
                    self.show_budget_status()

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
