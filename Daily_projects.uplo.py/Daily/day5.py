#1
num1 = 20
num2 = 6

print(num1 + num2)  # Addition
print(num1 - num2)  # Subtraction
print(num1 * num2)  # Multiplication
print(num1 / num2)  # Divition

#2
print(20 // 6)  # Floor Diviision
print(20 % 6)   # Modulus
print(2 ** 4)   # Exponent

#3
print(15 % 2)
print(10 % 5)
print(9 // 3)
print(5 * 3)

#4
print("===== RECEIPT =====")
item = input("Item: ").strip()
price = int(input("Price: "))
quantity = int(input("Quantity: "))
print()
print(f"Total: {price * quantity}")
print("===================")
