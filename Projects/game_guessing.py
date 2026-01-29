import random

def game_guessing():
    print("Wellcome to the 'guessing' game!!!")
    print("game: minecraft, valorant, roblox, gta")
    print("type (leave) to exit")

    games = [
        ("minecraft"),
        ("valorant"),
        ("roblox"),
        ("gta")
    ]
    secret_game = random.choice(games)

    while True:
        user_input = input("Enter your game: ").lower().strip()

        if user_input == 'leave':
            print(f"The game was {secret_game}. Better luck next time!")
            print("bye!")
            break

        if user_input == secret_game:
            print("Correct guess!")
            break

        else:
            print("Incorrect guess. Please try again.")
            print("game: minecraft, valorant, roblox, gta")

game_guessing()
