contacts = {}

while True:
    user_input = input("Enter(add contact, delete contact, edit contact, search contact, list contacts, exit): ").strip().lower()
    if user_input == "add contact":
        name = input("Enter contact name: ").strip()
        phone = input("Enter contact phone number: ").strip()
        email = input("Enter contact email: ").strip()
        company = input("Enter contact company: ").strip()
        contacts[name] = phone
        print(f"Contact '{name}' added successfully.")

    elif user_input == "delete contact":
        name = input("Enter a contact name to delete: ").strip()
        if name in contacts:
            del contacts[name]:
            print(f"contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")
            
    elif user_input == "edit contact":
        name = input("Enter a contact name to edit: ").strip()
        if name in contacts:
            new_name = input("Enter new contact name: ").strip()
            new_phone = input("Enter new phone contact: ").strip()
            new_email = input("Enter new email: ").strip()
            new_campany = input("Enter new campany: ").strip()
            del contacts[name]
            contacts[new_name] = new_phone
            print(f"the contact called '{name}' has been edited successfully.")
        else:
            print(f"contact '{name}' not found.")
    
    elif user_input == "search contact":
        name = input("Enter a contact name to search: ").strip()
        if name in contacts:
            print(f"contact '{name}' found: {contacts[name]}")
        else:
            print(f"contact '{name}' not found.")
    
    elif user_input == "list contacts":
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts found.")
    
    elif user_input == "exit":
        print("Exiting...")
        break

    else:
        print("Invalid command. Please try again.")
