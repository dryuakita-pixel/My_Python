#1
food = ["steak", "eggs"]

food.append("salmon")

print(food) #['steak', 'eggs', 'salmon']

food.remove("eggs")

print(food) #['steak', 'salmon']

#2
numbers = [10, 20, 30, 40]

numbers.pop(2)

print(numbers) #[10, 20, 40]

#3
numbers = [75, 92, 64, 88, 100]

numbers.append(1)
numbers.remove(64)
numbers.pop(1)
numbers.sort()

print(numbers) #[1, 75, 88, 100]
