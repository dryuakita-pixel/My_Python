#1
age = input("How old are you?: ")

print(age)
print(type(age))

#2
age = int(input("How old are you?: "))

print(age)
print(type(age))

#3
num1 = int(input("1st number: "))
num2 = int(input("2ns number: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

#4
name = input("What is your name?: ").strip()
num = int(input("How many pizzas: "))
price = int(input("Enter price: "))

print("-" * 25)
print(f"Customer: {name}")
print(num)
print(price)
print()
print(f"Total: {num * price}")
print("-" * 25)

#4
print("10" + "5")
print(10 + 5)
