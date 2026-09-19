name = input("Enter your name: ")
math = int(input("Enter your math score: "))
english = int(input("Enter your english score: "))
science = int(input("Enter your science score: "))

scores = [math, english, science]


def calculate_average(scores):
    return sum(scores) / len(scores)


def check_grade(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Very Good"
    elif average >= 75:
        return "Passed"
    else:
        return "Failed"


average = calculate_average(scores)
result = check_grade(average)


print("========================")
print("     STUDENT REPORT")
print("========================")
print(f"Name: {name}")
print(f"Math: {math}")
print(f"English: {english}")
print(f"Science: {science}")
print(f"Average: {average}")
print(f"Result: {result}")
print("========================")

print("\nINDIVIDUAL SUBJECT RESULTS:")

for score in scores:
    if score >= 75:
        print(f"{score} - Passed")
    else:
        print(f"{score} - Failed")