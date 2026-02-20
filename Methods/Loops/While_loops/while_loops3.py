while True:
    user_input = input(
        "(type 'leave' to exit)"
        "Enter your username here -> : "
    )

    if user_input == "leave":
        print("Goodbye")
        break 
    
    print("Nice to meet you,'",user_input,"'")
