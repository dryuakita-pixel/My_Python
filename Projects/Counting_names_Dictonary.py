counts = dict()
names = ['Jordan', 'MIcheal', 'Jordan', 'Mike', 'Micheal', 'Robert']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)