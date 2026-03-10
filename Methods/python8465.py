word = input("Enter any words -> : ")

while word == "":
    print("Please enter any words.")
    word = input("enter any words -> ")

user = word.split()
print(user)

while True:
    add = input("if you wanna add something type 'yes' or 'no' -> : ").lower()

    if add == "no":
        print("bye")
        break

    if add == "yes":
        new_word = input("enter any words -> : ")
        user.append(new_word)
        print(user)

    else:
        print("please type 'yes' or 'no'")
