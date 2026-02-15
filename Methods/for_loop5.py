print("type 'a' to count up to 1000")

letter = [
    'a'
]

while True:
    user_input = input("Enter the letter 'a': ")

    if user_input == 'a':
        for a in range(1001):
            print(a)
        break
