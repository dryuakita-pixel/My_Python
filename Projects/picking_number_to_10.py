#picking_number_to_10
def picking_number_to_10():
    print("Wellcome to the 'picking_number_to_10'")
    print("type 'leave' to exit")

    numbers = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10"
    ]

    while True:
        user_input = input("pick your number: ")

        if user_input == 'leave':
            print("Thank you for visiting!")
            break

        if user_input in numbers:
            print(f"{user_input} Great number pick!!!")
            break

picking_number_to_10()
