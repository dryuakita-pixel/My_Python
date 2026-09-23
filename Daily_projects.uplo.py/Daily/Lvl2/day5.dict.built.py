#1
profile = {}

profile["name"] = input("Enter your name: ")
profile["age"] = int(input("Enter your age: "))
profile["hobby"] = input("Enter your hobby: ")
profile["favorite_game"] = input("Enter your favorite game: ")

#2
profile = {}

profile["name"] = input("Enter your name: ")
profile["age"] = int(input("Enter your age: "))
profile["hobby"] = input("Enter your hobby: ")
profile["favorite_game"] = input("Enter your favorite game: ")

print("===== PROFILE =====")
print(f"Name: {profile['name']}")
print(f"Age: {profile['age']}")
print(f"Hobby: {profile['hobby']}")
print(f"Favorite Game: {profile['favorite_game']}")
print("===================")

#3
profile = {}

profile["name"] = input("Enter name: ")
profile["Age"] = int(input("Enter age: "))
profile["hobby"] = input("Enter hobby: ")
profile["fav_game"] = input("Enter favorite game: ")

print("===== PROFILE =====")
print(f"Name: {profile["name"]}")
print(f"Age: {profile['Age']}")
print(f"Hobby: {profile["hobby"]}")
print(f"Favorite game: {profile['fav_game']}")
print("===================")

if "hobby" in profile: 
    print("Hobby information found!")
else:
    print("Hobby information missing.")

#4
player = {}

player["name"] = input("Enter name: ")
player["game"] = input("Enter game: ")
player["lvl"] = int(input("Enter lvl: "))
player["fav_char"] = input("Enter fav character: ")

print("===== PLAYER PROFILE =====")
print(f"Name: {player["name"]}")
print(f"Game: {player["game"]}")
print(f"level: {player["lvl"]}")
print(f"fav_character: {player["fav_char"]}")
print("==========================")

if "lvl" in player:
    print("Level information found!")
else:
    print("Level information missing!")
