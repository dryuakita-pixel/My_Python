#1
student = {}

student["name"] = input("Enter name: ").strip()
student["age"] = int(input("Enter age: "))
student["fav_sub"] = input("Enter fav sub: ").strip()

#2
student = {}

student["name"] = input("Enter name: ").strip()
student["age"] = int(input("Enter age: "))
student["fav_sub"] = input("Enter fav sub: ").strip()
student["game"] = input("Enter your fav game: ").strip()

#3
student = {}

student["name"] = input("Enter name: ").strip()
student["age"] = int(input("Enter age: "))
student["fav_sub"] = input("Enter fav sub: ").strip()
student["game"] = input("Enter your fav game: ").strip()

if "game" in student:
    print("Game information found!")
else:
    print("Game information missing.")

#4
student = {}

student["name"] = input("Enter name: ").strip()
student["age"] = int(input("Enter age: "))
student["fav_sub"] = input("Enter fav sub: ").strip()
student["game"] = input("Enter your fav game: ").strip()

if "game" in student:
    print("Game information found!")
else:
    print("Game information missing.")

print("===== STUDENT INFO =====")
for key, value in student.items():
    print(f"{key}: {value}")
print("========================")

#5 mini challenge
player = {}

player["name"] = input("Enter name: ").strip()
player["game"] = input("Enter game: ").strip()
player["level"] = int(input("Enter lvl: "))
player["fav_char"] = input("Enter your favorite character: ").strip()

print("===== PLAYER PROFILE =====")
for key, value in player.items():
    print(f"{key}, {value}")
print("==========================")

if "level" in player:
    print("Level information found!")
else:
    print("non level")
