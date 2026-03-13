def Shopping_List_Builder():
    print("Wellcome to the Shopping list")
    print("type 'stop' to finish")

    shopping_list = []

    while True:
        user = input("Add itme (type 'stop' to finish) : ").lower()

        if user in shopping_list:
            print("Already in the list")
            continue

        if user == "stop":
            print(shopping_list)
            break

        elif user not in shopping_list:
            shopping_list.append(user)
            

Shopping_List_Builder()
