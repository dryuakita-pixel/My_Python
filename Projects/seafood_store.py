def seafood_store():
    print("wellcome to seafood store")
    print("we have: salmon, squid, tuna, octopus, fish, crab, lobster, shrimp")
    print("type 'leave' to exit")

    while True:
        seafood = [
            ("salmon"),
            ("squid"),
            ("tuna"),
            ("octopus"),
            ("fish"),
            ("crab"),
            ("lobster"),
            ("shrimp"),
        ]

        user_input = input("What do you want do get?: ")

        if user_input == 'leave':
            print("thank you for coming in our store!")
            break

        if user_input == 'salmon':
            print("Here is your shrimp! Was there anything else you wanted to get?")
        elif user_input == 'squid':
            print("Here is your squid! Was there anything else you wanted to get?")
        elif user_input == 'tuna':
            print("Here is your tuna! Was there anything else you wanted to get?")
        elif user_input == 'octopus':
            print("Here is your octopus! Was there anything else you wanted to get?")
        elif user_input == 'fish':
            print("Here is your fish! Was there anything else you wanted to get?")
        elif user_input == 'crab':
            print("Here is your crab! Was there anything else you wanted to get?")
        elif user_input == 'lobster':
            print("Here is your lobster! Was there anything else you wanted to get?")
        elif user_input == 'shrimp':
            print("Here is your shrimp! Was there anything else you wanted to get?")
        else:
            print("Invalid seafood. Please try again.")

seafood_store()
