print("contacts: 'alex', 'mike', 'mark'")

contacts = {
    "alex": "09012345678",
    "mike": "09809800980",
    "mark": "90870067565"
}

while True:
    user = input("Enter the name of the contact: ")

    if user in contacts:
        print(contacts[user])

    else:
        print("Contact not found.")
