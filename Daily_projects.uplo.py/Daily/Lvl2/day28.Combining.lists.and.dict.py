#1
games = [
    {"name": "Mineacraft", "year": 2011},
    {"name": "Roblox", "year": 2005}
]

print(games[0]["name"])
print(games[1]["year"])

#2
players = [
    {"name": "Nathan", "level": 10},
    {"name": "Alex", "level": 15}
]

print(players[0]["level"])
print(players[1]["name"])

#3
players = [
    {"name": "Nathan", "level": 10},
    {"name": "Alex", "level": 15}
]

players.append({
    "name": "John", "level": 20,
})

print(players[0]["level"])
print(players[1]["name"])
print(players[2]["level"])
