contact = {}

while True:
    user_input = input("'add contact', 'delete contact', 'view contact', 'edit contact', 'search contact', 'leave' to exit").strip().lower()

    if user_input == "leave":
        print("leaving...")
        break

    elif user_input == "add contact":
        name = input("Enter contact name: ").strip()
        phone = input("Enter contact phone: ").strip()
        email = input("Enter contact email: ").strip()
        company = input("Enter contact company: ").strip()
        contact[name] = {
            "phone": phone,
            "email": email,
            "company": company
        }
        print("Successfully added contact.")

    elif user_input == "delete contact":
        name = input("Enter a contact name to delete: ").strip()
        if name in contact:
            user_remove = input("Are you sure You wanna delete this contact? (yes) or (no): ").strip()
            if user_remove == "yes":
                del contact[name]
                print("Successfully deleted contact.")
            elif user_remove == "no":
                print("Delete, discontinued.")
        else:
            print(f"Contact '{name}' was not found.")

    elif user_input == "view contact":
        if not contact:
            print("NO contact found.")
        else:
            for name, contact_info in contact.items():
                print(f"Name: {name}.")
                print(f"Phone: {contact_info[phone]}.")
                print(f"Email: {contact_info[email]}")
                print(f"company: {contact_info[company]}") 
    
    elif user_input == "edit contact":
        name_contact = input("Enter the name of the contact to edit it: ").strip()
        if name_contact in contact:
            new_name = input("Enter to new name: ").strip()
            new_phone = input("Enter the new phone: ").strip()
            new_email = input("Enter new email: ").strip()
            new_company = input("Enter new company").strip()
            del contact[name]
            contact[new_name] = {
                 "new_name": new_name,
                 "new_phone": new_phone,
                 "new_email": new_email,
                 "new_company": new_company
            }
            print(f"'{new_name}' was Successfully edited.")
        else:
            print(f"{name} contact was not found.")

    elif user_input == "search contact":
        name = input("Enter the contact that you wanna search: ").strip()
        
        if name in contact:
            info = contact[name]
            print(f"Name: {name}.")
            print(f"Phone: {contact_info[phone]}.")
            print(f"Email: {contact_info[email]}.")
            print(f"company: {contact_info[company]}.")
        else:
            print("Contact was not found.")

    else:
        print("Invalid")
