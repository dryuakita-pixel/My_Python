1print("The goal is to get 5 points")

score = 0

input1 = input("what is 4 / 2? : ")
if input1 == "2":
    print("correct!")
    score += 1
else:
    print("Wrong answer! the correct answer is 2")

input2 = input("What is 14 / 7? :")
if input2 == "2":
    print("correct!")
    score += 1
else:
    print("Wrong answer! the correct answer is 2")

input3 = input("What is 10 / 5? :")
if input3 == "2":
    print("correct!")
    score += 1
else:
    print("Wrong answer! the correct answer is 2")

input4 = input("what is 38 / 19? : ")
if input4 == "2":
    print("correct!")
    score += 1
else:
    print("Wrong answer! the correct answer is 2")

input5 = input("what is 100 / 50? : ")
if input5 == "2":
    print("correct!")
    score += 1
else:
    print("Wrong answer! the correct answer is 2")

print(f"Your final score is: {score}/4")
