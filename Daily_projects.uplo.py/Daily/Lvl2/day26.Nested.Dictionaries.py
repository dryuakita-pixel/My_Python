#1
player = {
    "info": {
        "name": "Nathan",
        "level": 25
    }
}

print(player["info"]["level"]) #Output: 25

#2
game = {
    "Details": {
        "name": "Minecraft",
        "year": 2011
    }
}

print(game["Details"]["name"]) #Output: Minecraft

#3
student = {
    "Profile": {
        "name": "Nathan",
        "age": 14
    },
    "scores": {
        "math": 90,
        "english": 85
    }
}

print(student["Profile"]["name"])
print(student["Profile"]["age"])
print(student["scores"]["math"])
print(student["scores"]["english"])
