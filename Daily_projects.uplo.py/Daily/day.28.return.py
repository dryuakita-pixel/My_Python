#1
def add(a, b):
    return a + b

result = add(10, 5)
print(result)

#2
def multiply(a, b):
    return a * b
    
result = multiply(8, 8)
print(result)

#3
def greeting(name):
    return f"Hello, {name}!"
    
message = greeting("Nathan") #output: Hello, Nathan
print(message)

#4
def calculate_average(math, english, science):
    return math + english + science
    
average = calculate_average(90, 80, 100)
print(average / 3) #output: 90.0