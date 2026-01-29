def user_input():
    print("type 'leave' to exit")

    while True:
        user_input = input("Type anything you wanted: ")

        if user_input == 'leave':
            print("Thenk you for visiting!")
            break
        
        if user_input:
            print("You typed: " + user_input)

user_input()
