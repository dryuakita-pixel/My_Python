#1
foods = {"Eggs", "Rice", "Chicken", "Banana"}

print("Rice" in foods)
print("Eggs" in foods)

#2
hobbies = {"Basketball", "Programming", "Gaming"}

if "Programming" in hobbies:
    print("Hobby found")
else:
    print("Hobby not found")

#3
games = {"Minecraft", "Roblox", "Fortnite", "Bedwars"}

game_name = input("Enter a game: ").strip()

if game_name in games:
    print("game found!")
else:
    print("game not found.")
