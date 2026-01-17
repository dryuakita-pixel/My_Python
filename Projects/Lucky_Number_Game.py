import random

print("wolcome to the 'lucky Number' game.")

guess = int(input("enter a number between 1 and 5: "))

secret_number = random.randint(1, 5)
print(secret_number)

if guess == secret_number:
    print("Correct!")

else:
    print("Incorrect.")
