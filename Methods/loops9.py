print("type on the anything to print it 10x!!!")
print("type 'leave' to exit")

while True:
    user_input = input("type here. : ")

    if user_input == 'leave':
        print("thank you for visiting!")
        break

    for a in range(11):
        print(user_input)
        
