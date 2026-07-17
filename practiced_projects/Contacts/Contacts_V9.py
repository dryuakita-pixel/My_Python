def contact_v9():
    contacts = {}
    
    while True:
        print("-" * 120)
        user_input = int(input("Enter numbers only.\n(1) Add contacts\n(2) Delete contacts\n(3) Edit contact\n(4) View\n(5) Search\n(6) Exit\nEnter here -> : "))
        print("-" * 120)

        if user_input == 6:
            print("leaving...")
            break

        elif user_input == 1:
            name = input("Enter contact name: ").strip()

            if name in contacts:
                print("Contact already exists.")
                continue
            phone = input(f"Enter {name} phone number: ").strip()
            email = input(f"Enter {name} email: ").strip()
            company = input(f"Enter {name} company(Enter blank if non): ").strip()
            contacts[name] = {
                "phone": phone,
                "email": email,
                "company": company
            }

        elif user_input == 2: 
            name_delete = input("Enter an existing name to delete: ").strip()

            if name_delete not in contacts:
                print(f"{name_delete} is not in contacts.")
                continue

            else:
                del contacts[name_delete]
                print(f"{name_delete} has been deleted from contacts.")
            
        elif user_input == 3:
            name_edit = input("Enter an existing name to edit: ").strip()

            if name_edit not in contacts:
                print(f"{name_edit} is not in contacts.")
                continue

            else:
                pick = int(input("Pick which one to edit\n(1) name\n(2) phone\n(3) email\n(4) company\nEnter here -> : "))
                if pick == 1:
                    new_name = input("Enter new name: ").strip()
                    if new_name in contacts:
                        print("Contact already exists.")
                        continue
                    contacts[new_name] = contacts.pop(name_edit)
                elif pick == 2:
                    new_phone = input("Enter new phone number: ").strip()
                    contacts[name_edit]["phone"] = new_phone
                elif pick == 3:
                    new_email = input("Enter new email: ").strip()
                    contacts[name_edit]["email"] = new_email
                elif pick == 4:
                    new_company = input("Enter new company: ").strip()
                    contacts[name_edit]["company"] = new_company

        elif user_input == 4:
            if len(contacts) == 0:
                print("No contacts to view.")
                continue

            else:
                print("Total contacts:", len(contacts))
                for name, info in contacts.items():
                    print(f"name: {name}")
                    print(f"Phone: {info['phone']}")
                    print(f"Email: {info['email']}")
                    print(f"company: {info['company']}")

        elif user_input == 5:
            search = input("Enter a name to search: ").strip()
            if search not in contacts:
                print(f"{search} is not in contacts.")
                continue
            else:
                info = contacts[search]
                print(f"name: {search}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"company: {info['company']}")

contact_v9()
