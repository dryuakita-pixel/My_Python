def adition_user_number():
    print("Wellcome to the adition user number program!")
    
    user = int(input("Please enter a number: "))
    adition = int(input("Please enter a number to add it by: "))

    result = user + adition

    print(f"The result: {user} + {adition} = {result}")

adition_user_number()
