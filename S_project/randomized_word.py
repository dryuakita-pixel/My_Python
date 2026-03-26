import random

def randomize_words():
    print("Type words to add to the list.")
    print("Type 'done' when you are finished.")

    words = []

    while True:
        user = input("Enter a word -> : ")

        if user.lower() == 'done':
            print(random.choice(words))
            break
        
        if user == "":
            print("You didn't type anything.")
            continue

        words.append(user)
        print(f"added {user}")
        
randomize_words()
