def get_name():
    print("names": Alice, Bob, Charlie, David, Eve")

names = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve"
]

while True:
    name = input("Enter a name (or type 'leave' to exit ->: ").strip()

    if name == "leave":
        print("Exiting the program. Goodbye!")
        break

    if name in names:
        if name == "Alice":
            print("Happy valentine's day,", name[:5], "!!!")
        elif name == "Bob":
            print("Happy valentine's day,", name[:3], "!!!")
        elif name == "Charlie":
            print("Happy velentine's day,", name[:7], "!!!")
        elif name == "David":
            print("Happy velentine's day,", name[:5], "!!!")
        elif name == "Eve":
            print("Happy valentinve's day,", name[:3], "!!!")
        else:
            print("Invalid name, Please try again.")
            continue
