#1
person = {
    "name": input("Enter name:"),
    "age": input("Enter age: "),
    "Fav_food": input("Enter fav food: ")
}

print(person)

#2
person = {
    "name": input("Enter name:"),
    "age": input("Enter age: "),
    "fav_food": input("Enter fav food: ")
}

print(person["name"])
print(person["age"])
print(person["fav_food"])

#3
person = {
    "name": input("Enter name:"),
    "age": input("Enter age: "),
    "fav_food": input("Enter fav food: ")
}

person["fav_food"] = input("Enter new fav food: ")
print(person)

#4
player = {
    "name": input("Enter player name: "),
    "game": input("Enter Game: "),
    "lvl": input("Enter Level: "),
    "fav_charac": input("Enter fav character: ")
}

print("===== PLAYER PROFILE =====")
print(f"Name: {player['name']}")
print(f"Game: {player['game']}")
print(f"Level: {player['lvl']}")
print(f"Favorite Character: {player['fav_charac']}")
print("==========================")
