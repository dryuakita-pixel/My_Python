def contactsV5():

    contacts = {}
    total_contacts = 0

    while True:

        print("-" * 120)
        user_input = input("(1) 'add contact'\n(2) 'delete contact'\n(3) 'edit contact'\n(4) 'view contact'\n(5) 'search contacts'\n(6) 'leave'\n -> : ").strip()
        print("-" * 120)

        if user_input == "6":
            print("Leaving...")
            break

        elif user_input == "1":
            name = input("Name: ").strip()
            if name in contacts:
                print("Contact already exists...")
                continue
            phone = input("Phone number: ").strip()
            email = input("Email address: ").strip()
            company = input("Company: ").strip()
            total_contacts += 1
            contacts[name] = {
                "name": name,
                "phone": phone,
                "email": email,
                "company": company,
            }
            print("sucessfully added.")

        elif user_input == "2":
            name = input("Name: ").strip()
            if name in contacts:
                choice = input(f"Are you sure you want to delete {name}? (y/n): ").strip()
                if choice == "y":
                    total_contacts -= 1
                    del contacts[name]
                    print("sucessfully deleted.")

        elif user_input == "3":
            name = input("Name: ").strip()
            if name in contacts:
                choice = input(f"(1) 'Phone number'\n(2) 'Email address'\n(3) 'Company'\n -> : ").strip()
                if choice == "1":
                    new_phone = input("New phone number: ").strip()
                    contacts[name]["phone"] = new_phone
                    print("sucessfully edited.")

                elif choice == "2":
                    new_email = input("New emial address: ").strip()
                    contacts[name]["email"] = new_email
                    print("sucessfully edited.")

                elif choice == "3":
                    new_company = input("New company name: ").strip()
                    contacts[name]["company"] = new-company
                    print("sucessfully edited.")

            else:
                print(f"could't find {name}.")

        elif user_input == "4":
            if not contacts:
                print("No contacts found.")
            else:
                print(f"Total contacts: {total_contacts}")
                for name, info in contacts.items():
                    print(f"Name: {name}")
                    print(f"Phone: {info['phone']}")
                    print(f"Email: {info['email']}")
                    print(f"Company, {info['company']}")

        elif user_input == "5":
            name = input("Search contact: ").strip()
            if name in contacts:
                print(f"Name: {name}")
                print(f"Phone: {phone}")
                print(f"Email: {email}")
                print(f"Company: {company}")
            else:
                print(f"couldn't find {name}.")

        else:
            print(f"{user_input} is not valid.")

contactsV5()
