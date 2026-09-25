#1
player = {
    "name": "Nathan",
    "game": "Roblox",
    "lvl": 2800
}

for key, value in player.items():
    print(key, value)

#2
player = {
    "name": "Nathan",
    "game": "Roblox",
    "lvl": 2800
}

for k, v in player.items():
    print(f"{k}: {v}")

#3
student = {
    "name": "Nathan",
    "age": 14,
    "grade": 9,
    "hobby": "basketball"
}

for key, val in student.items():
    print(f"{key}: {val}")

#4
game = {
    "name": "Minecraft",
    "genre": "Sandbox",
    "lvl": 50,
    "platform": "PC"
}

print("===== GAME INFO =====")

for names, values in game.items():
    print(f"{names}: {values}")

print("=====================")
