# calculator.py
# A simple calculator using functions and error handling

# Define the calculator function that performs the operation
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"


# Function to safely get a numeric input from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


# Function to get a valid operator from the user
def get_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("Choose operator (+, -, *, /): ").strip()
        if operator in valid_operators:
            return operator
        else:
            print("❌ Invalid operator. Please choose from +, -, *, /.")


# Main program block
try:
    print("=== Simple Calculator ===")

    # Get user inputs safely
    num1 = get_number("Enter the first number: ")
    operator = get_operator()
    num2 = get_number("Enter the second number: ")

    # Try performing the calculation
    try:
        result = calculator(num1, num2, operator)
        print(f"\n✅ Result: {num1} {operator} {num2} = {result}")
    except OverflowError:
        print("❌ Error: Number too large to handle.")

# Handle user interruption (Ctrl+C)
except KeyboardInterrupt:
    print("\n❗ Calculation cancelled by user.")

# Handle unexpected EOF (Ctrl+D on Linux/macOS)
except EOFError:
    print("\n❗ Input ended unexpectedly.")

# Catch any other unexpected error
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
