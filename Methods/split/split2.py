user = input("enter enything : ")

while user == "":
    print("you did not enter anything")
    user = input("enter anything : ")

word = user.split()
print(word)
