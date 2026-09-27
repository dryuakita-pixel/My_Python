#1
player = {
    "name": "Nathan",
    "level": 25
}

if player["level"] >= 20:
    print("Good level!")
else:
    print("keep playing")

#2
player = {
    "name": "Nathan",
    "level": 25
}

if player["level"] >= 50:
    print("Very high level!")
elif player["level"] >= 20:
    print("Good level!")
else:
    print("Keep playing!")

#3
player = {}

player["name"] = input("Enter your name: ").strip()
player["level"] = int(input("Enter your age: "))

if player["level"] >= 20:
    print("Good level!")
else:
    print("Keep playing.")

#4
student = {}

student["name"] = input("Enter your student name: ").strip()
student["ave_score"] = int(input("Enter your avearage score: "))

print("===== STUDENT RESULT =====")
print(f"Name: {student["name"]}")
print(f"Average: {student['ave_score']}")

if student["ave_score"] >= 90:
    student["result"] = ("Exellent")
elif student["ave_score"] >= 80:
    student["result"] = ("Very Good!")
elif student["ave_score"] >= 75:
    student["result"] = ("Passed")
else:
    student["result"] = ("Failed")

print(f"Result: {student['result']}")

print("==========================")
