#1 dictionary
player = {
    "name": "Nathan",
    "level": 20,
    "game": "Minecraft"
} #Output: Minecraft

print(player["game"])

#2 Tuples
games = ("Minecarft", "Roblox", "Valorant")

print(games[1]) #Output: Roblox

#3
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

total_set = set1 | set2
print(total_set) #Output: {1, 2, 3, 4, 5, 6}

intersection_set = set1 & set2
print(intersection_set) #Output: {3, 4}

different_set = set1 - set2
print(different_set) #Output: {1, 2}

#4
students = [
    {"name": "Nathan", "score": 95},
    {"name": "Alex", "score": 88}
]

print(students[0]["score"]) #Output: 95
print(students[1]["name"]) #Output: Alex

#5
classroom = {
    "teacher": "Mr. Smith",
    "students": ["Nathan", "Alex", "John"]
}

print(classroom["students"][1]) #Output: Alex
