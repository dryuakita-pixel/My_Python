print("The goal is to get 5 points")

score = 0

input1 = input("What is 2 + 2? : ")
if input1 == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong answer! the correct answer is 4.")

input2 = input("What is 5 + 3? : ")
if input2 == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong answer! the correct answer is 8.")

input3 = input("What is 10 + 7! : ")
if input3 == "17":
    print("Correct!")
    score += 1
else:
    print("Wrong answer! the correct answer is 17.")

input4 = input("What is 38 + 12? : ")
if input4 == "50":
    print("correct!")
    score += 1
else:
    print("Wrong answer! the correct answer is 50.")

input5 = input("What is 101 + 99? : ")
if input5 == "200":
    print("Correct!")
    score += 1
else:
    print("Wrong answer! the correct answer is 200.")

print(f"Your final score is {score} out of 5!")
