def calculator():
    print("Welcome to terminal calculator")
    print("Type 'leave' to exit")

    while True:
        operation = input("\noperation (+ - * /) or 'leave': ").lower()

        if operation == 'leave':
            break

        if operation in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if operation == '+':
                print(f"result: {num1 + num2}")
            elif operation == '-':
                print(f"result: {num1 - num2}")
            elif operation == '*':
                print(f"result: {num1 * num2}")
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero")
                else:
                    print(f"result: {num1 / num2}")
        else:
            print("Invalid operation. Please try again.")

if __name__ == "__main__":
    calculator()
