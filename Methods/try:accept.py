#try/accept
print("ami: do you wanna go to the park?")
print("type 'yes' or 'no' or type 'leave' to exit")

while True:
    user_input = input(":")

    if user_input == 'leave':
        print("thank you for visiting!")
        break
    
    elif user_input == 'yes':
        print("Okay lets go!")
        break
    elif user_input == 'no':
        print("Okay then...")
        break
