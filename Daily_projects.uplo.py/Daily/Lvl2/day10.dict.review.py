#1
student = {}

student["name"] = input("Enter name: ").strip()
student["age"] = int(input("Enter age: "))
student["fav_subject"] = input("Enter your fav sub: ").strip()
student["ave_score"] = int(input("Enter your average score: "))

if student["ave_score"] >= 90:
    student["result"] = "Excellent"
elif student["ave_score"] >= 80:
    student["result"] = "Very Good"
elif student["ave_score"] >= 75:
    student["result"] = "Passed"
else:
    student["result"] = "Failed"

print("===== STUDENT PROFILE =====")
for key, val in student.items():
    print(f"{key}: {val}")
print("===========================")

if "result" in student:
    print("Result information found!")
else:
    print("Result information missing.")

print("===========================")

