age = int(input("What is your age: "))

while age < 0:
    print("Please enter a valid age, please try again.")
    age = int(input("What is your age: "))

print("your age is ", age)
