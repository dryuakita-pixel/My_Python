import random

print("Wellcome to 'type this'")

fruits = ["apple", "banana", "cherry", "mango"]
fruit = random.choice(fruits)

print(f"tpye this : {fruit}")
user = input("here -> : ")

if user == fruit:
    print("correct.")
else:
    print(f"wrong, it was {user}. Better luck next time!")
