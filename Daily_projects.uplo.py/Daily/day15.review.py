#1 B
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

#2 Practice
age = 14
has_ball = True

if age >= 14 and has_ball:
    print("Practice!")
else:
    print("Cannot practice.")

#3 Not allowed
age = 12
has_permission = True

if age >= 13:
    if has_permission:
        print("Allowed")
else:
    print("Not allowed")

#4
score = int(input("Enter score: "))

if score >= 90:
    print("exellent!")
elif score >= 80:
    print("Very Good")
elif score >= 75:
    print("Passed")
else:
    print("Failed")

#5
age = int(input("Age: "))
has_ball = True

if age >= 13 and has_ball:
    print("Ready to practice")
else:
    print("Connot practice")

#6
username = input("Enter username: ").strip()
password = input("Enter pass: ").strip()

if username == "nathan909":
    if password == "909asdf9090":
        print("Login succesfully")
    else:
        print("Wrong pass")
else:
    print("Wrong username")
