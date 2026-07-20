def check_number(number):
    if number > 1:
        return "Positive"
    elif number < -1:
        return "Negative"
    else:
        return "Zero"
    
result = check_number(5)
print(result)
