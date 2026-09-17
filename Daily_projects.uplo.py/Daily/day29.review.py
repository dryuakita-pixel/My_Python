#1
def sqaure(number):
    print(number * number)
    
sqaure(5)

#2
def multiply(a, b):
    return a * b
    
result = multiply(5, 3)
print(result)

#3
scores = [65, 82, 91, 74, 95, 60]

for score in scores:
    if score >= 75:
        print(score)

#4
scores = [65, 82, 91, 74, 95, 60]

def check_scores(scores):
    for score in scores:
        if score >= 75:
            print(f"Passed: {score}")
        else:
            print(f"Failed: {score}")   
                     
check_scores(scores)
