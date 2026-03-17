print("welcome to the TODO list")
print("type 'leave' to exit.")

todo = []

while True:
    user = input("Add task: ")
    
    if user == "leave":
        print(f"here is your todo list: {todo}")
        print("bye bye")
        break

    todo.append(user)
