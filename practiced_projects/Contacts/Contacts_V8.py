def Contacts_V8():
    contacts = {}
    total_contacts = 0
    
    while True:
        print("-" * 120)
        user_input = input("Enter only number.\n(1) 'create contact'\n(2) 'delete contacts'\n(3) 'edit contact'\n(4) 'search contacts'\n(5) 'view contacts'\n(6) 'exit'\n-> : ").strip()
        print("-" * 120)

        if user_input == "6":
            print("Exiting...")
            break

        elif user_input == "1":
            name = input("Enter name: ").strip()
            if name in contacts:
                print("Contact already exists.")
                continue
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            choice = input(f"Does this contacts have company? (y/n) -> : ").strip()
            if choice.lower() == "y":
                company = input("Enter company: ").strip()
            elif choice.lower() == "n":
                company = "N/A"
            else:
                print("Invalid input.")
            contacts[name] = {
                "phone": phone,
                "email": email,
                "company": company
            }
            total_contacts += 1

        elif user_input == "2":
            name = input("Enter name to delete contact.").strip()
            choice = input(f"Are you sure you want to delete {name}? (y/n) -> : ").strip()
            if choice.lower() == "y":
                if name in contacts:
                    del contacts[name]
                    total_contacts -= 1
                    print(f"{name} has been deleted.")
            elif choice.lower() == "n":
                print("Deletion cancelled.")
                continue
            else:
                print("Invalid input.")

        elif user_input == "3":
            name = input("Enter name to edit contacts").strip()
            if name in contacts:
                choice = input("Enter number to edit:\n(1) 'name'\n(2) 'phone number'\n(3) 'email'\n(4) 'company'\n-> : ").strip()
                if choice == "1":
                    new_name = input("Enter new name: ").strip()
                    if new_name in contacts:
                        print("Contact already exists.")
                    else:
                        contacts[new_name] = contacts[name]
                        del contacts[name]
                elif choice == "2":
                    new_phone = input("Enter new phone number: ").strip()
                    contacts[name]["phone"] = new_phone
                elif choice == "3":
                    new_email = input("Enter new email: ").strip()
                    contacts[name]["email"] = new_email
                elif choice == "4":
                    new_company = input("Enter new company: ").strip()
                    contacts[name]["company"] = new_company
                else:
                    print("Invalid input.")

        elif user_input == "4":
            name = input("Enter name to search contact. -> : ").strip()
            if name in contacts:
                print(f"Name: {name}")
                print(f"Phone: {contacts[name]['phone']}")
                print(f"Email: {contacts[name]['email']}")
                print(f"Company: {contacts[name]['company']}")
            else:
                print("Contact not found.")

        elif user_input == "5":
            if not contacts:
                print("No contacts found.")
            else:
                print(total_contacts)
                for name, info in contacts.items():
                    print(f"Name: {name}")
                    print(f"Phone: {info['phone']}")
                    print(f"Email: {info['email']}")
                    print(f"Company: {info['company']}")


Contacts_V8()
