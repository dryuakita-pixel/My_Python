class User:
    def __init__ (self, name, age, country, email):
        self.name = name
        self.age = age
        self.country = country
        self.email = email
        input1 = input("Enter your name: ")
        input2 = input("Enter your age: ")
        input3 = input("Enter your country: ")
        input4 = input("Enter your email: ")

        while True:
            if input1 and input2 and input3 and input4:
                self.name = input1
                self.age = input2
                self.country = input3
                self.email = input4
                break
            
            else:
                print("All fields are required. Please try again.")
            
        print(f"Hi! your name is {self.name}, you are {self.age} years old, you are from {self.country}, and your email is {self.email}.")

user1 = User("","","","")
