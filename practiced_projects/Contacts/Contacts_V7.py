def Contacts_V7():
    contacts = {}
    total_contacts = 0

    while True:
        print("-" * 120)
        user_input = input("Enter number\n(1) 'add contact'\n(2) 'delete contact'\n(3) 'edit contact'\n(4) 'search contact'\n(5) 'view contacts'\n(6) 'exit'\n-> : ").strip()
        print("-" * 120)

        if user_input == "6":
            print("Exiting...")
            break

        elif user_input == "1":
            name = input("Name: ").strip()
            if name in contacts:
                print(f"{name} already exists in contacts.")
                continue
            phone = input("Phone number: ").strip()
            email = input("Email address: ").strip()
            company_input = input("does the contact have a company? (y/n): ").strip().lower()
            if company_input == "y":
                company = input("Company name: ").strip()
            elif company_input == "n":
                company = None
            else:
                print("Invalid input.")
                continue
            total_contacts += 1
            contacts[name] = {
                "phone": phone,
                "email": email,
                "company": company
            }

        elif user_input == "2":
            name = input("Enter name to delete: ").strip()
            if name in contacts:
                choice = input(f"Are you user you wanna delete '{name}'? (y/n): ").strip().lower()
                if choice == "y":
                    del contacts[name]
                    print(f"{name} has been deleted.")
                elif choice == "n":
                    print("Deletion cancelled.")
                else:
                    print("Invalid input.")
            else:
                print(f"{name} not found in contacts.")
                continue

        elif user_input == "3":
            name = input("Enter name to edit: ").strip()
            if name in contacts:
                choice = input("Enter number\n(1) 'edit phone number'\n(2) 'edit email address'\n(3) 'edit company name'\n-> : ").strip()
                if choice == "1":
                    new_phone = input("New phone number: ").strip()
                    contacts[name]["phone"] = new_phone
                    print("Phone number updated.")
                    continue
                elif choice == "2":
                    new_email = input("New email address: ").strip()
                    contacts[name]["email"] = new_email
                    print("Email address updated.")
                    continue
                elif choice == "3":
                    new_company = input("New company: ").strip()
                    contacts[name]["company"] = new_company
                    print("Company updated.")
                    continue
                else:
                    print("valid option.")
            else:
                print(f"{name} not found in contacts.")
                continue
        
        elif user_input == "4":
            name = input("Enter name to search: ").strip()
            if name in contacts:
                print(f"Name: {name}")
                print(f"Phone number: {contacts[name]['phone']}")
                print(f"Email address: {contacts[name]['email']}")
                if contacts[name]["company"]:
                    print(f"Company: {contacts[name]['company']}")
                else:
                    print("Company: None")
            else:
                print(f"{name} not found in contacts.")
                continue
        
        elif user_input == "5":
            if not contacts:
                print("No contacts found.")
            else:
                print(f"total contacts is {total_contacts}")
                for name, info in contacts.items():
                    print(f"Name: {name}")
                    print(f"Phone number: {info['phone']}")
                    print(f"Email address: {info['email']}")
                    if info["company"]:
                        print(f"Company: {info['company']}")
                    else:
                        print("Company: None")

Contacts_V7()
