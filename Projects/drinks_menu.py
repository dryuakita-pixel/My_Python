def drinks_menu():
    print("welcome to the drinks_menu.")
    print("drinks: coffee, tea, juice, milk, water")
    print("type 'leave' to exit")
    
    drinks = [
        "coffee",
        "tea",
        "juice",
        "milk",
        "water",
    ]
    
    while True:
        user_input = input("Enter your menu: ")
        
        if user_input == 'leave':
            print("Thank you for visiting!")
            break
            
        if user_input in drinks:
            print(f"One {user_input} coming right up!")
        else:
            print("Sorry, we don't have that.")

drinks_menu()
