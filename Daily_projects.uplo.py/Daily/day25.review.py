games = ["Minecreaft", "Roblox", "MLBB", "bedwars"]

#1
print(games)
print(games[0])
print(games[3])
games[2] = "sniper_arena"
print(games)
print(len(games))

#2
games.append("GTA")
games.remove("Roblox")
games.pop(0)
games.sort()
print(games)

#3
scores = [65, 82, 91, 74, 95, 60]
print(scores)

for score in scores:
    if score >= 75:
        print(score)

#4
scores1 = [55, 90, 72, 88, 64, 95, 79]

print(scores1)

for score1 in scores1:
    if score1 >= 75:
        print(score1)

scores1.append(100)
scores1.remove(55)
scores1.sort()
print(scores1)
