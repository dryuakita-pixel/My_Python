name = input("What is your name?: ").strip()

while name == '':
    print("you did't enter a name.")
    name = input("What is your name?: ").strip()

print("Hello " + name + ", " + "How are you today?")
