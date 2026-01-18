points = [
    ("hen", 2100),
    ("cow", 3200),
    ("pig", 2520),
]

first = []

for name, point in points.items():
    first.append((point, name))
    
    print(sorted(first, reverse=True))
