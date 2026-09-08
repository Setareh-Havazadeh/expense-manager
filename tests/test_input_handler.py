from input_handler import InputHandler

def test_input_handler( monkeypatch):

    input_handler = InputHandler()
    inputs = iter(["5", "Test"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))  # Simulate user input of 5
    # Test numeric_input with valid input
    assert input_handler.numeric_input() == 5  # Simulate user input of 5

    # Test text_input with valid input
    assert input_handler.text_input() == "Test"  # Simulate user input of "Test"

def test_input_handler_invalid_numeric_input(monkeypatch):
    input_handler = InputHandler()
    inputs = iter(["-1", "7"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))  # Simulate user input of 7

    # Simulate invalid numeric input followed by valid input
    assert input_handler.numeric_input() == 7  # Simulate user input of -1, then 7

def test_input_handler_invalid_input(monkeypatch):
    input_handler = InputHandler()
    inputs = iter(["text", "7"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))  # Simulate user input of 7

    # Simulate invalid numeric input followed by valid input
    assert input_handler.numeric_input() == 7  # Simulate user input of text, then 7

def test_input_handler_invalid_text_input(monkeypatch):
    input_handler = InputHandler()
    inputs = iter(["456", "Valid Input"])
    monkeypatch.setattr("builtins.input", lambda: "Valid Input")  # Simulate user input of "Valid Input"

    # Simulate invalid text input followed by valid input
    assert input_handler.text_input() == "Valid Input"  # Simulate user input of "456", then "Valid Input"
