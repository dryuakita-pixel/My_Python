username = input("Enter username : ")

while username == "":
    print("Your username is empty.")
    username = input("Enter username : ")

    if len(username) <= 5:
        print("Your username must be at least 5 character long.")
        username = input("Enter username : ")

        user = username.replace(" ", "")
    

print(f"Hello, {username.strip()}.")
