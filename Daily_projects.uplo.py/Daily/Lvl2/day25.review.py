#1
games = {"Minecraft", "Roblox", "Minecraft"}

print(len(games)) #output: 3

#2
player = {
    "name": "Nathan",
    "games": ["MInecraft", "Roblox", "Fortnite"]
}

print(player["name"])
print(player["games"][1])

#3
player1 = {"Minecraft", "Roblox", "Fortnite"}
player2 = {"Minecraft", "Valorant", "Fortnite"}

all_games = player1 | player2
print(all_games)  # Output: {'Minecraft', 'Roblox', 'Fortnite', 'Valorant'}

games_have = player1 & player2
print(games_have) # Output: {'Fortnite', 'Minecraft'}

only_games = player1 - player2
print(only_games) #Output: {'Roblox'}
