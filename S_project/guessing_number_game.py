import random

numbers = random.randint(1, 10)
guess = int(input("Guess number between 1 and 10: "))

if numbers == guess:
    print("Corract!!!")

else:
    print(f"Wrong, the right number is {numbers}.")
