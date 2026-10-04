#1
games = {"Minecraft", "Roblox", "Minecraft", "Fortnite", "Roblox"}

print(games) #output: {'Minecraft', 'Fortnite', 'Roblox'}

#2
foods = {"Eggs", "Rice", "chiken"}

foods.add("Steak")
foods.remove("chiken")
print(foods) #output: {'Rice', 'Eggs', 'Steak'}

#3
games = {"Minecraft", "Roblox", "Minecraft", "Bedwars"}

print(games) #output: {'Roblox', 'Bedwars', 'Minecraft'}

games.add("Fortnite")
games.remove("Roblox")
print(games) #output: {'Fortnite', 'Bedwars', 'Minecraft'}
