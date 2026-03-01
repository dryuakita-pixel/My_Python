#while looping the leter and adding the len() method too.
user = input("type anything: ")

while user == "":
    print("you did not type anything")
    user = input("type anything: ")

print(f"your '{user}' has {len(user)} on it.")
