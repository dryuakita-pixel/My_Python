#1
foods1 = {"Eggs", "Rice"}
foods2 = {"Steak", "Banana"}

all_foods = foods1 | foods2
print(all_foods)

#2
games1 = {"Minecarft", "Roblox", "Fortnite"}
games2 = {"Minecarft", "Fortnite", "Bedwars"}

common_games = games1 & games2
print(common_games)

#3
foods1 = {"Eggs", "Rice", "Steak"}
foods2 = {"Rice", "Chiken", "Banana"}

common_foods = foods1 & foods2
print(common_foods)

#4
player1 = {"Minecarft", "Roblox", "Fortnite"}
player2 = {"Minecarft", "Fornite", "Bedwars"}

all_games = player1 | player2

common_games = player1 & player2

print("===== GAME COMPARISON =====")
print(f"All Games: {all_games}")
print(f"Common Games: {common_games}")
print("===========================")
