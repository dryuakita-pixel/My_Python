print("The key is '123'")

key = {
    "123"
}

while key != '123':
    key = input("type the key here -> : ")

    if key != '123':
        print("wrong key, please try again.")

    if key == '123':
        print("correct key!")
