def restaurant():
    print("Welcome to the restaurant")
    print("The menu: burger, pizza, taco, pasta")

menu = ("burger, pizza, taco, pasta")

while True:
    restaurant()
    user_input = input("What would you like to order: ").lower().strip()

    if user_input in menu:
        if user_input == 'burger':
            print("The buger will be here in 5mins!")
        elif user_input == 'pizza':
            print("Your pizza will be here in 15mins!")
        elif user_input == 'taco':
            print("Your taco will be here in 10mins!")
        elif user_input == 'pizza':
            print("Your pizza will be here in 20mins!")
    else:
        print("Your order are invalid. Please try again.")
