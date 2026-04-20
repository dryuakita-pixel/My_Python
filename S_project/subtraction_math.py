print("The goal is to get 5 points")

score = 0

input1 = input("What it 8 - 4? :")
if input1 == "4":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong answer! it was 4")

input2 = input("What is 15 - 5? : ")
if input2 == "10":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong answer! it was 10")

input3 = input("What is 20 - 8? :")
if input3 == "12":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong answer! it was 12")

input4 = input("What is 30 - 15? :")
if input4 == "15":
    print("correct! +1 point")
    score += 1
else:
    print("Wrong answer! it was 15")

input5 = input("What is 50 - 25? :")
if input5 == "25":
    print("Correct! +1 point")
    score += 1
else:
    print("wrong answer! it was 25")

print(f"Your final score is: {score} out of 5!")
