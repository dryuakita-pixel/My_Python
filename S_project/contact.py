contacts = {}

while True:
    action = input("Enter: 'add', 'view', 'search' or 'exit': ").lower()
    if action == "add":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif action == "view":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    elif action == "search":
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(f"{search_name}: {contacts[search_name]}")
        else:
            print("contact not found.")

    elif action == "exit":
        print("Exiting...")
        break
    
    else:
        print("Invalid action. Please try again.")
