contact = {}
total_contacts = 0

while True:
    print("-" * 120)
    user_input = input("(1) 'add contact'\n(2) 'delete contact'\n(3) 'view` contact'\n(4) 'edit contact'\n(5) search contact\n(6) 'exit'\nEnter a number here -> : ").strip()
    print("-" * 120)

    if user_input == "6":
        print("exiting...")
        break

    elif user_input == "1":
        name = input("Enter contact name: ").strip()
        if name in contact:
            print(f"{name} already existed.")
            continue
        phone = input("Enter contact phone number: ").strip()
        email = input("Enter contact email: ").strip()
        company = input("Enter contact company: ").strip()
        contact[name] = {
            "phone": phone,
            "email": email,
            "company": company
        }
        total_contacts += 1
        print(f"Total contacts: {total_contacts}")

    elif user_input == "2":
        name = input("Enter contact name to delete: ").strip()
        if name in contact:
            user_delete = input(f"Do you want to delete {name}? (y/n) ").strip()
            if user_delete == "y":
                total_contacts -= 1
                del contact[name]
                print(f"Successfully deleted {name}.")
            elif user_delete == "n":
                print("Delete discontinued.")
        else:
            print(f"{name} not found.")

    elif user_input == "3":
        if not contact:
            print("No contacts found.")
        else:
            print(f"Total contacts: {total_contacts}")
            for name, info in contact.items():
                print("-" * 30)
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"company: {info['company']}")

    elif user_input == "4":
        name = input("Enter contact name to edit: ").strip()
        if name in contact:
            contact_change = input(f"What do you want to edit?\n(1) 'phone'\n(2) 'email'\n(3) 'company'\nEnter a number here -> ").strip()
            if contact_change == "1":
                new_phone = input("Enter contact new phone number: ").strip()
                contact[name]["phone"] = new_phone
                print(f"Successfully edited {name}.")
            elif contact_change == "2":
                new_email = input("Enter contact new email address: ").strip()
                info = contact[name]["email"] = new_email
                print(f"Successfully edited {name}.")
            elif contact_change == "3":
                new_company = input("Enter contact new company: ").strip()
                info = contact[name]["company"] = new_company
                print(f"Successfully edited {name}.")
        else:
            print(f"{name} not found.")

    elif user_input == "5":
        name = input("Enter contact name to search: ").strip()
        if name in contact:
            print(f"Name: {name}")
            print(f"Phone: {contact[name]['phone']}")
            print(f"Email: {contact[name]['email']}")
            print(f"Company: {contact[name]['company']}")
        else:
            print(f"{name} not found.")

    else:
        print("Invalid input.")
