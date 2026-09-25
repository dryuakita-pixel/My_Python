#1 examples
player = {
    "name": "Nathan",
    "game": "Minecraft",
    "lvl": "35"
}

print(player.keys())
print(player.values())

#2 useing keys
player = {
    "name": "Nathan",
    "game": "Minecraft",
    "lvl": "35"
}

for key in player.keys():
    print(key)

#3 using values
player = {
    "name": "Nathan",
    "game": "Minecraft",
    "lvl": "35"
}

for value in player.values():
    print(value)

#4
student = {
    "name": "Nathan",
    "age": 14,
    "grade": 9,
    "hobby": "basketball"
}

print("====Keys=====")
for key in student.keys():
    print(key)

print("=====Values=====")
for value in student.values():
    print(value)
