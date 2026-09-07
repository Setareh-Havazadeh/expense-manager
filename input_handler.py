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
