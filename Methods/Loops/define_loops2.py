def get_names():
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    print("Available names:", ", ".join(names))
    return names


names = get_names()

while True:
    name = input("Enter a name (or type 'leave' to exit): ").strip()

    if name.lower() == "leave":
        print("Exiting the program. Goodbye!")
        break

    if name in names:
        print(f"Happy Valentine's Day, {name}!!!")
    else:
        print("Invalid name. Please try again.")
