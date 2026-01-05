
password = "pass123" # Match the password variable

while True: # Fixed: True (capitalized)
    attempt = input("Enter your password: ").strip()

    if attempt == password:
        print("Password is granted")
        break

    else:
        print("Password is incorrect") # Fixed typo
