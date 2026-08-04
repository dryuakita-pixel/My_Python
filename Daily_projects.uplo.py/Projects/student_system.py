print("Questions:")
name = input("Enter student name: ").strip()
age = int(input("Enter age: "))
grade = int(input("Enter Grade Level: "))
subject = input("Enter favorite subject: ").strip()
math = int(input("Enter Math score: "))
english = int(input("Enter English score: "))

print("-" * 50)
print(f"(STUDENT INFORMATION)\n(Name: {name}) (Age: {age}) (Grade Level: {grade})\nFavortie Subject: {subject}\nMath Score: {math}\nEnglish: {english}\nAverage: {(math + english) / 2}")
average = (math + english) / 2

print(f"Passed: {average >= 75}")
print(f"Math Higher Than English: {math > english}")
print(f"English higher than Math: {english > math}")
print("-" * 50)
