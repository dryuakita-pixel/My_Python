name = input("type a messy word : ")

while name == "":
    print("you did not type a messy word.")
    name = input("type a messy word : ")

print(f"the {name} you typed will be turn into {name.title()} by the '.tittle' method.")
