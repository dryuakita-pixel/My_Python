student = [
    {
        "name": "Nathan",
        "scores": [90, 85, 88]
    },
    {
        "name": "Alex",
        "scores": [80, 75, 92]
    }
]

print(student[0]["name"]) #Output: Nathan
print(student[0]["scores"][0]) #Output: 90
print(student[1]["name"]) #Output: Alex
print(student[1]["scores"][2]) #Output: 92

average = sum(student[0]["scores"]) / len(student[0]["scores"])
print(average)

if average >= 75:
    result = "Passed"
else:
    result = "Failed"

print("=====================")
print(f"Name: {student[0]["name"]}")
print(f"Scores: {student[0]["scores"]}")
print(f"Average: {average}")
print(f"Result: {result}")
print("=====================")
