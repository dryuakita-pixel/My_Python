#1
foods1 = {"Eggs", "Rice", "Chicken"}
foods2 = {"Rice", "Chicken", "Banana"}

only_foods1 = foods1 - foods2
print(only_foods1)

#2
school = {"Math", "English", "Science"}
favorite = {"Math", "Science", "Basketball"}

subjects = school - favorite
things = favorite - school

print(f"Subjects in school but not favorite: {subjects}")
print(f"Things in favorite but not in school: {things}")

#3
player1 = {"Minecraft", "Roblox", "Fortnite", "Bedwars"}
player2 = {"Minecraft", "Fortnite", "Valorant", "Bedwars"}

only_player1 = player1 - player2
only_player2 = player2 - player1

print("===== UNIQUE GAMES =====")
print(f"Player 1 only: {only_player1}")
print(f"Player 2 only: {only_player2}")
print(f"========================")
