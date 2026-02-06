def terminal_restaurant():
        print("Welcome to the restaurant!")
        print("menu: curry, omelette, steak, chiken, wagyu, pork. bread: croissant, sourdough, flatbread, brioche. desert: icecream, cupcake, cake, pie, brownie")
        print("type 'leave' to exit.")

        menu = [
                "curry",
                "omelette",
                "steak",
                "chiken",
                "wagyu",
                "pork",
                "croissant",
                "sourdough",
                "flatbread",
                "brioche",
                "icecream",
                "cupcake",
                "cake",
                "pie",
                "brownie"
        ]
        count = {}

        while True:
                user_input = input("Enter your menu[type 'done' to finish.: ").lower()
                
                if user_input == 'leave':
                        print("Thank you for visiting.")
                        return

                if user_input == 'done':
                        print("We will order it for you.")
                        break

                if user_input in menu:
                        count[user_input] = count.get(user_input, 0) + 1

                else:
                        print("Invalid input. Please try again.")

        print("\nYour order count:")
        for dish, times in count.items():
                print(dish, "=", times)

terminal_restaurant()
