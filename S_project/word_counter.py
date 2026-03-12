user = input("Enter a sentence : ")

while user == "":
    print("You did not type a sentence.")
    user = input("Enter a sentence : ")

split = user.split()
print(split)
print((len(split)))
