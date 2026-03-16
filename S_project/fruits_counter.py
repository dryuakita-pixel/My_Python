print("fruits: apple, banana, orange.")
print("type 'leave' to quit")

fruits = {}

while True:
    fruit = input("Enter a fruit: ")

    if fruit == "leave":
        print(fruits)
        break

    if fruit in fruits:
        fruits[fruit] += 1
    else:
        fruits[fruit] = 1
