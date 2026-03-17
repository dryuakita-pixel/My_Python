total_num = 0

while True:
    user = input("Enter grocery items: ")

    if user == "leave":
        print(f"Total: {total_num}")
        print("bye.")
        break

    item, total = user.split()
    total = int(total)

    total_num += total
