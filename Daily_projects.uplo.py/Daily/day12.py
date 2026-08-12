#1
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter")
else:
    print("You cannot enter")

#2
day = input("Enter the day: ")

if day == "Saturday" or day == "Sunday": 
    print("it's the weekend!")
else:
    print("It's school day.")

#3
raining = False

if not raining:
    print("You can play basketball today!")
else:
    print("Stay inside")

#4
age = int(input("Enter age: "))
has_ball = True

if age >= 14 and has_ball:
    print("You can practice")
else:
    print("You need to meet the requirements first.")

#5
age = 14
has_ball = False

if age >= 14 and has_ball:
    print("A")
else:
    print("B")
