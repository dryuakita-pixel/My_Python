#1
game = {
    "name": "Minecraft",
    "stats": (100, 50, 25)
}

print(game["name"])
print(game["stats"])
print(game["stats"][2])

#2
student = {
    "name": "Nathan",
    "stats": (85, 90, 95)
}

print(student["name"])
print(student["stats"][0])
print(student["stats"][2])

#3
player = {
    "name": "Chungyx",
    "game": "Roblox",
    "stats": (34,67,43)
}

print("===== PLAYER PROFILE =====")
print(f"Name: {player["name"]}")
print(f"Game: {player["game"]}")
print(f"First stats: {player['stats'][0]}")
print(f"Second stats: {player["stats"][1]}")
print(f"Thrid stats: {player["stats"][2]}")
print("==========================")
