def desert_menu():
    print("welcome to the 'desert_menu;")
    print("desert: icecream, cupcake, cake, pie, brownie")
    print("type 'leave' to exit")

    desert = [
        ("icecream"),
        ("cupcake"),
        ("cake"),
        ("pie"),
        ("brownie")
    ]

    while True:
        user_input = input("Enter your menu: ")

        if user_input == 'leave':
            print("Thank you for visiting!")
            break

        if user_input == 'icecream':
            print("Here is your icecream!")
        elif user_input == 'cupcake':
            print("here is your cupcake!")
        elif user_input == 'cake':
            print("here is your cake!")
        elif user_input == 'pie':
            print("Here is your pie!")
        elif user_input == 'cupcake':
            print("Here is your cupcake!")
        elif user_input == 'brownie':
            print("Here is your brownie!")
        else:
            print("Invalid input. Please try again.")
            print("desert: icecream, cupcake, cake, pie, brownie")

desert_menu()
