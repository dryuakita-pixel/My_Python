#1
foods = ("Eggs", "Chiken", "Rice", "Banana")

for food in foods:
    print(food)

#2
numbers = (12, 25, 40, 55, 70)

for number in numbers:
    if number >= 40:
        print(number)

#3
scores = (90, 73, 56, 23, 78, 53)

for score in scores:
    if score >= 75:
        print(f"passed: {score}")
    else:
        print(f"Failed: {score}")
