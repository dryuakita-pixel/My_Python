#1
age = int(input("Enter your age: "))

if age >= 13:
    if age <= 17:
        print("You are a teenager.")

  #2
  age = int(input("Enter age: "))
level = int(input("Enter game level: "))

if age >= 13:
    if level >= 10:
        print("Acces granted!")
    else:
        print("Level too low.")
if age <= 13:
    print("Age requirement not met.")

#3
age = int(input("Enter age: "))
has_ball = True

if age >= 13:
    if has_ball:
        print("Ready to practice.")
    else:
        print("You need a basketball.")
if age <= 13:
    print("Age requirement not met.")

#4
username = input("Enter Username: ").strip()
password = input("Enter password: ").strip()

if username == "Nathan1":
    if password == "909zx9090":
        print("Login Successful")
    else:
        print("Wrong Password!")
else:
    print("Wrong username")
