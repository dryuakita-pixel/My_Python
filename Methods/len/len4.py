user_name = input("Enter your user name : ")

while user_name == "":
    print("you did not write a user name.")
    user_name = input("Enter your user name : ")

    if len(user_name) < 1-5:
        print("Invalid username it must be at least 5 characters long.")
    elif len(user_name) > 20:
        print("Invalid username. your username must be less than 20 characters.")
   
print(f"Hello {user_name}! your username is {len(user_name)}")
