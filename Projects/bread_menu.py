def bread_menu():
    print("The bread menu: croissant, sourdough, baguette, flatbread, brioche, focaccia")
    print("type pause to exit.")

breads = ["croissant", "sourdough", "baguette", "flatbread", "brioche", "focaccia"]

while True:
    bread_menu()
    user_input = input("Enter the bread you wanted: ").lower().strip()

    if user_input == "pause":
        break
    elif user_input in breads:
        if user_input == "croissant":
            print("Here is your croissant!.")
        elif user_input == "sourdough":
            print("Here is your sourdough!")
        elif user_input == "baguette":
            print("Here is your baguette!")
        elif user_input == "flatbread":
            print("Here is your flatbread!")
        elif user_input == "brioche":
            print("Here is your brioche!")
        elif user_input == "focaccia":
            print("Here is your focaccia!")
    else:
        print("Invalid bread type. Please try again.")
