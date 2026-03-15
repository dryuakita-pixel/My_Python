print("fruits: apple, banana, orange.")
print("type 'leave' to quit")

fruit_count = {}

while True:
    user = input("Enter your fruits: ").lower()

    if user == "leave":
        print("bye bye.")
        print(fruit_count)
        break

    fruits = user.split()

    for fruit in fruits:
        if fruit in fruit_count:
            fruit_count[fruit] += 1
        else:
            fruit_count[fruit] = 1
