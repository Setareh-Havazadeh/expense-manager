class InputHandler:
    def numeric_input(self):
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

    def text_input(self):

        while True:
            text = input()
            if not text.isdigit() and len(text.strip()) > 0:
                break
            else:
                print("Please search again and enter the correct text!! ")

        return text

    def get_expenses(self):

        print(
            "Enter the number of expenses you wish to add to the list as a numerical value."
        )
        expense_count = self.numeric_input()
        expenses = []
        for _ in range(expense_count):

            print("Please enter the title:")
            title = self.text_input()
            print("Please enter the amount: ")
            amount = self.numeric_input()
            print("Please enter the category: ")
            category = self.text_input()
            expenses.append({"title": title, "amount": amount, "category": category})
        return expenses
