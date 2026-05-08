# Topic 1 — OOP (Object-Oriented Programming)

# Without OOP, code becomes messy:
user1_name = "Sam"
user1_age = 23

user2_name = "Ram"
user2_age = 20

#Class = Blueprint
#Object = Real thing created from blueprint

# Basic class Example
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"my name is {self.name} and I am {self.age} years old")

