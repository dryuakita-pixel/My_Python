name = input("Enter student name: ").strip()
math = int(input("Enter math score: "))
english = int(input("Enter english score: "))
science = int(input("Enter science score: "))

average = (math + english + science) // 3

print("-" * 30)
print("STUDENT PERFORMANCE:")
print("-" * 30)
print(f"Name: {name}")
print(f"Math: {math}")
print(f"English: {english}")
print(f"Science: {science}")
print(f"Average: {average}")
if average >= 90:
    print("Exelent performance!")
    if math >= 90:
        print("Exelent at math!")
    else:
        print("Good job!")
elif average >= 80:
    print("Very good")
elif average >= 75:
    print("Passed")
else:
    print("Failed")
print("-" * 30)
