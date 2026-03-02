word = input("type anything : ")

while word == "":
    print("you did not type anything.")
    word = input("type anything : ")

print(f"the length of your word '{word}' is '{len(word)}'.")
