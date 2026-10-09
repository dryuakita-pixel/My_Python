#1
available_foods = {"Eggs", "Rice", "Chicken", "Fish"}
my_foods = {"Rice", "Chicken", "Beef"}

print(my_foods.issubset(available_foods))

#2
available_games = {"Minecraft", "Roblox", "Fortnite"}
mygames = {"Minecraft", "Roblox"}

print(mygames.issubset(available_games))

#3
available_items = {"Sword", "Shield", "Potion", "Bow"}
inventory = {"Sword", "Potion"}

print(inventory.issubset(available_items))  # True
print(available_items.issubset(inventory))  # False
