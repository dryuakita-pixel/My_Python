def Contacts_V6():
    contacts = {}
    total_contacts = 0
    
    while True:
        print("-" * 120)
        user_choice = input("(1) 'add contact'\n(2) 'delete contact'\n(3) 'edit contact'\n(4) 'search'\n(5) 'view contacts'\n(6) 'exit'\n-> :").strip()
        print("-" * 120)

        if user_choice == "6":
            print("Exiting...")
            break
        
        elif user_choice == "1":
            name = input("Name: ").strip()
            if name in contacts:
                print(f"{name} already exists in contacts.")
                continue
            phone = input("Phone number: ").strip()
            email = input("Email address: ").strip()
            company = input("Company: ").strip()
            contacts[name] = {
                "phone": phone,
                "email": email,
                "company": company
            }
            total_contacts += 0
            print(f"contact '{name}' added successfully.")
            
        elif user_choice == "2":
            name = input("Enter name to delete: ").strip()
            if name in contacts:
                choice = input(f"Are you sure you want to delete '{name}'? (y/n) -> : ").strip()
                if choice == "y":
                    del contacts[name]
                    total_contacts -= 1
                    print(f"contact '{name}' deleted successfully.")
                elif choice == "n":
                    print("Delete cancelled.")

        elif user_choice == "3":
            name = input("Enter name to edit: ").strip()
            if name in contacts:
                choice = input("(1) 'edit name'\n(2) 'edit phone number'\n(3) 'edit email address'\n(4) 'edit company'\n-> : ").strip()
                if choice == "1":
                    new_name = input("Enter new name: ").strip()
                    contacts[name]["name"] = new_name
                    print(f"'{new_name} was successfully edited.")
                elif choice == "2":
                    new_phone = input("Enter new phone number: ").strip()
                    contacts[name]["phone"] = new_phone
                    print(f"'{new_phone}' was successfully edited.")
                elif choice == "3":
                    new_email = input("Enter new email address: ").strip()
                    contacts[name]["email"] = new_email
                    print(f"'{new_email}' was successfully edited.")
                elif choice == "4":
                    new_company = input("Enter new company: ").strip()
                    contacts[name]["company"] = new_company
                    print(f"'{new_company}' was successfully edited.")
                else:
                    print("Invalid choice. Edit cancelled.")
                    continue
            else:
                print(f"{name} does not exist in contacts.")

        elif user_choice == "4":
            name = input("Enter name to search: ").strip()
            if name in contacts:
                print(f"Name: {name}")
                print(f"Phone number: {contacts[name]['phone']}")
                print(f"Email address: {contacts[name]['email']}")
                print(f"Company: {contacts[name]['company']}")
            else:
                print(f"{name} does not exist in contacts.")

        elif user_choice == "5":
            if not contacts:
                print("No contacts to display.")
            else:
                for name, info in contacts.items():
                    print(f"Name: {name}")
                    print(f"Phone number: {info['phone']}")
                    print(f"Email address: {info['email']}")
                    print(f"Company: {info['company']}")

        else:
            print("Invalid input. Please try again.")
            
Contacts_V6()
