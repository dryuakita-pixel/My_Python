#1
name = input("What's your name? ").strip()
age = input("How old are you? ").strip()
color = input("What's your favorite color? ").strip()

print(name)
print(age)
print(color)

#2
def add_profile(name, age, color):

    print("-" * 30)
    print(f"Profile:\nName: {name}\nAge: {age}\nColor: {color}")
    print("-" * 30)

add_profile("Nathan", 14, "green")

#3
name = input("name: ")
job = input("job: ")
country = input("country: ")
Fav_coding_lang = input("Fav_coding_lang: ")

print("-" * 30)
print(name)
print(job)
print(country)
print(Fav_coding_lang)
print("-" * 30)
