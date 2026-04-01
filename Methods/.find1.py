def finding_user_stucture():
    print("type 'leave' to exit")
    text = input("type anything here to add to the list: ").strip()

    while True:
        letter = input("Enter the part of the word that you want to find: ").strip()
        
        if letter == 'leave':
            print("bye.")
            break

        user_structure = text.find(letter)

        if user_structure == -1:
            print(f" this letter is not in the text: {text}")
        
        else:
            print(f"This letter is found at index: {user_structure} in the text: {text}")

finding_user_stucture()
