def main_dish():
        print("Welcome to the main dish!")
        print("dish: curry, omelet, steak, stew")
        print("type 'leave' to exit")

        dish = [
                ("curry"),
                ("omelet"),
                ("steak"),
                ("stew")
        ]

        while True:
                user_input = input("Enter your dish: ")

                if user_input == 'leave':
                        print("Thank you for visiting!")
                        break
                if user_input == 'curry':
                        print("Here is your curry! what else would you like to order?")
                elif user_input == 'omelet':
                        print("Here is your omelet! what else would you like to order?")
                elif user_input == 'steak':
                        print("Here is your steak! what else would you like to order?")
                elif user_input == 'stew':
                        print("Here is your stew! what else would you like to order?")
                else:
                        print("Invalid input. Please try again.")
                        print("dish: curry, omelet, steak, stew")
                        
main_dish()
