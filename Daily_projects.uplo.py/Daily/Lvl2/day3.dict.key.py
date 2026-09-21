#1
student = {
    "name": "Nathan",
    "age": 14,
    "grade": 8
}

print("student" in student)
print("age" in  student)
print("name" in student)

#2
student = {
    "name": "Nathan",
    "age": 14,
    "grade": 8
}

if "name" in  student:
    print("name exists!")
else:
        print("name is not stored.")
if "school" in student:
    print("school exists!")
else:
        print("school is not stored.")
    
#3
player = {
    "name": "Nathan",
    "game": "Minecraft",
    "lvl": 30
}

if "lvl" in player:
    print("Level information found!")
else:
    print("Level information missing.")
    