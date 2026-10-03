#1
player = {
    "name": "Nathan",
    "game": "Minecraft",
    "level": 50
}

print(player["name"])
print(player["level"])

#2
scores = (80, 95, 70)

print(scores[0])
print(scores[1])
print(scores[-1])

#3
player = ("Nathan", 14, "Basketball")

name, age, hobby = player

print(name)
print(age)
print(hobby)

#4
scores = (60, 85, 92, 70, 95)

for score in scores:
    if score >= 75:
        print(f"Passed: {score}")
    else:
        print(f"Failed: {score}")

#5
student = {
    "name": "Nathan",
    "scores": (45, 56, 98)
}

print(student["name"])
print(student["scores"][0])
print(student["scores"][1])
print(student["scores"][-1])

average = (student["scores"][0] + student["scores"][1] + student["scores"][-1]) / 3
print(average)

if average >= 75:
    print("Passed")
else:
    print("Failed")
