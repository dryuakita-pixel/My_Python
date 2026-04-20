1print("The goal is to get 5 points")

score = 0

input1 = input("What is 3 x 6? : ")
if input1 == "18":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong answer! it was 18")

input2 = input("What is 2 x 4? : ")
if input2 == "8":
    print("correct! +1 point")
    score += 1
else:
    print("Wrong answer! it was 8")

input3 = input("What is 5 x 5? : ")
if input3 == "25":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong answer! it was 25")

input4 = input("What is 7 x 3? : ")
if input4 == "21":
    print("correct! +1 point")
    score += 1
else:
    print("Wrong answer! it was 21")

input5 = input("What is 9 x 2? : ")
if input5 == "18":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong answer! it was 18")

print(f"You final score is: {score} points")
