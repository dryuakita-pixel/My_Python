#1
num1 = 10
num2 = 5

print(num1 == num2)
print(num1 != num2)
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)

#2
num1 = 20
num2 = 20

print(num1 == num2)
print(num1 != num2)
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)

#3
age = int(input("your age: "))
print(age >= 18) #False

#4 - Age Checker
age = int(input("Enter Your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
