def meat_factory():
    print("Wellcome to the meat factory!")
    print("meat: chiken, wagyu, beef, pork, ")
    print("type exit to leave.")

    while True:
        meat = [
            ("chiken"),
            ("wagyu"),
            ("beef"),
            ("pork"),
        ]
        user_input = input("Enter the meat you wanted (type 'leave' to exit): ").lower().strip()

        if user_input.lower() == ("leave"):
            print("Thank you for using the meat factory!")
            break

        if user_input == "chiken":
            print("Here is your chiken!")
        elif user_input == "wagyu":
            print("Here is your wagyu!")
        elif user_input == "beef":
            print("Here is your beef!")
        elif user_input == "pork":
            print("Here is your pork!")
        else:
            print("Invalid meat. Please try again.")

meat_factory()
