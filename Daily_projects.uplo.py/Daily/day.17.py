#1
number = int(input("Enter a number: "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter another number: "))

#2
attempts = 1

while attempts <= 3:
    print("Attempt:", attempts)
    attempts = attempts + 1

#3
pas = input("Enter pass: ").strip()

while pas != "909asdf":
    print("Wrong pass.")
    pas = input("Enter pass: ").strip()

print("Correct pass.")

#4
secret = 7
guess = int(input("Guess the number: "))

while guess != 7:
    print("Wrong, try again!")
    guess = int(input("Guess the number: "))

print("Correct guess!")
