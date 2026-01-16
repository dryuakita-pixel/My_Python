import random

animal = ["chiken", "cow", "pig", "ostrich", "bird", "parrot", "owl"]
secret.anmimal = rondom.choice(animal)
guessed_letters = []
attempts = 5

print("Wellcome to the guessing game!")

def jls_extract_def(secret):
    while attempts > 0:
        displey_word = ""
        for latter in secret.animal:
            if latter in guessed_letters:
                display_animal += latter + ""
            else:
                desplay_animal += "_ "
    return display_animal


def jls_extract_def(secret):
    display_animal = jls_extract_def(secret)
    return display_animal


def jls_extract_def(secret):
    display_animal = jls_extract_def(secret)
    return display_animal


def jls_extract_def(secret):
    display_animal = jls_extract_def(secret)
    return display_animal


display_animal = jls_extract_def(secret)

print(f"/nanimal: {display_animal}")
print(f"Attempts left: {attempts}")
print(f"letters guessed: {', '.join(guessed_letters)}")

guess = input("guess a letter: ").lower()

if len (guess) is 1 or not guess.isalpha():
    print("you already guessed that letter.")
    continue

guessed_letters.append(guess)

if guess in secret_word:
    print guess in secret_animal:
    pirnt(f"great job! '{guess}' is in the animal.")
else:
    print(f"sorry, '{guess}' is not in the animal.")
    attempts -= 1")

    if all(letter in guessed_letters for letter in secret_animal):
        print(f"congratulations! you guessed the animal: {secret_animal}")
        break
    else:
        print(f"\ngame over. the word was: {secret_animal}")
