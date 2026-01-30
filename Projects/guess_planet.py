import random

def guess_planet():
    print("Wellcome to the 'guessing_planet'")
    print("planet: mars, moon, jupiter, earth, saturn")
    print("type 'leave' to exit")

    world = [
        "mars",
        "moon",
        "jupiter",
        "earth",
        "saturn"
    ]
    secret_planet = random.choice(world)

    while True:
        user_input =  input("Enter: ")

        if user_input == 'leave':
            print("Thank you for visiting!")
            break

        if user_input == secret_planet:
            print("Correct guess!")
            break

        else:
            print("Incorrect guess. Please try again.")
            print("planet: mars, moon, jupiter, earth, saturn")

guess_planet()
