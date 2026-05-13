contacts = {}
total_contacts = 0

while True:
    print("-" * 120)
    user_input = input("(1) 'add contact'\n(2) 'delete contact'\n(3) 'edit contact'\n(4) 'view contact'\n(5) 'search contact'\n(6) 'exit'\nEnter here -> : ").strip()
    print("-" * 120)

    if user_inputcontacts == "6":
        print("Exiting...")
        break

    elif user_input == "1":
        name = input("Name:: ").strip()
        if name in contacts:

            print("This contact already exists...")
            continue
        phone = input("Phone number: ").strip()
        email = input("Email: ").strip()
        company = input("Company name: ").strip()

        contacts[nmae] = {
            "name": name,
            "phone": phone,
            "email": email,
            "company": company
        }
        total_contacts += 1

    elif user_input == "2":
        name = input("Name: ").strip()
        if name in contacts:

            choice = input(f"Do you want to delete {name}? (y/n): ").strip()
            if choice == "y":
                total_contacts -= 1
                del contacts[name]

            elif choice == "n":
                continue

    elif user_input == "3":
        name = input("Search contact: ").strip()
        if name in contacts:

            choice = input("Edit: (1) 'Name'\n(2) 'Phone number'\n(3) 'Email'\n(4) 'Company'\nEnter here -> : ").strip()
            if choice == "!":
                new_name = input("New name: ").strip()
                contacts[name]["name"] = new_name
                print("succesfully edited!")

            elif choice == "2":
                new_phone = input("New phone number: ").strip()
                contacts[name]["phone"] = new_phone
                print("succesfully edited!")

            elif choice == "3":
                new_email = input("New email: ").strip()
                contacts[name]["email"]  = new_email
                print("succesfully edited!")

            elif choice == "4":
                new_company = input("New company: ").strip()
                contacts[name]["company"] = new_company
                print("succesfully edited!")

        else:
            print(f"{name} not found...")

    elif user_input == "4":
        if not contacts:

            print("No contacts found...")
            continue

        else:
            print(f"total contacts: {total_contacts}")
            for name, info in contacts.items():

                print("-" * 40)
                print(f"Name: {name}")
                print(f"Phone number: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Company: {info['company']}")
                print("-" * 40)

    elif user_input == "5":
        name = input("Search contact: ").strip()
        if name in contacts:

            print(f"name: {name}")
            print(f"Phone number: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
            print(f"Company: {contacts[name]['company']}")

        else:
            print(f"{name} not found...")

