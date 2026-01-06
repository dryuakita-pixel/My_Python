counts = dict()
names = ['Jordan', 'Micheal', 'Jordan', 'Mike', 'Micheal','Mike', 'Robert', 'Mike',]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)
