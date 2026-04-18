def terminal_calculator():
    print("Wellcome to the Terminal Calculator!")
    print("type 'exit' to quit the calculator")
    
    while True:
        input1 = input("Enter the first number here -> : ")
        input3 = input("Enter the operator here (+, -, *, /) -> : ")
        input2 = input("Enter the second number here -> : ")

        if input1.lower() == 'exit' or input2.lower() == 'exit' or input3.lower() == 'exit':
            print("Thank you for using the Terminal Calculator!")
            break

        try:
            num1 = float(input1)
            num2 = float(input2)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if input3 == '+':
            result = num1 + num2
        elif input3 == '-':
            result = num1 - num2
        elif input3 == '*':
            result = num1 * num2
        elif input3 == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                continue
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            continue

        print(f"The result is: {result}")
