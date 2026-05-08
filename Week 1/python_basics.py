# Unit 1.1

# Variables and Data Types
"""
name = "Tanmay"  # name stores text (string)
age = 21    # age stores number (int)

amount = 9.99  # price is in point which is stored in float

is_student = True  # boolean is where we store value in True/False
"""

# print - used to print values/statements
"""
print(age)
print(name)
print(amount)
"""

# f-string
"""
print("my name is"+name) #instead of using this we use f-string method
print(f"my name is {name} and I am {age} years old")  #better way
"""

# taking user input
"""
name = input("Enter your name: ")
print(f"Hello {name}")
"""

# Unit 1.2

# If Else Condition ->


#Boolean values -> always Returns 2 options - True or False
"""
age = 20
print(age>=18)

print(10>5)
print(5 == 5)
print(4 != 9)
"""

# Basic if statement
"""
age = 20

if age >= 18:
    print("You are adult")
"""

# If else condition - Used when 2 possible outcome and only 1 executes
"""
age = 15

if(age>18):
    print("You are Adult")
else:
    print("You are minor")
"""

# If elif else - Used when multiple conditions exists
"""
marks = 85

if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 50:
    print("C Grade")
else:
    print("Fail")
"""

# LOOPS

#without loops
"""
print("hello world")
print("hello world")
print("hello world")
"""

#with loops
"""
for i in range(3):
    print("hello world")
"""

# Two main type of loops : For and While

# 1. For Loop

"""
for i in range (5):
    print(i)
"""

#custom range
"""
for i in range(1,6):
    print(i)
"""

# Loop through Strings
"""
name = "Tanmay"

for letter in name:
    print(letter)
"""

# 2. While Loop -> Runs while condition is true
"""
count = 1
while count<=5:
    print(count)
    count += 1
"""

# Functions

#without functions
"""
print("Hello world")
print("Hello world")
print("Hello world")
"""

# with functions
"""
def Hello:
    print("Hello world")

Hello()
Hello()
Hello()
"""

# Functions with Parameters
"""
def hello(name):  # this is parameter
    print(f"Hello {name}")

hello("tanmay")   # this is argument
"""

# functions with return values
"""
def add(a,b):
    return a+b

result = add(5,3)
print(result)
"""

# Default parameter arguments

def my_function(name = "Friend"):
    print(f"{name} is my friend")

my_function("Tanmay")
my_function("Emily")
my_function()



# Lists, Tuples, and Dictionaries


# 1.Lists

fruits = ["apple","banana","mango"]

#accessing items
"""
print(fruits[0])
print(fruits[1])
print(fruits[2])
"""

# Add items
"""
fruits.append("orange")
print(fruits)
"""

# remove items
"""
fruits.remove("mango")
print(fruits)
"""

# Loop through List
"""
for fruit in fruits:
    print(fruit)
"""


# 2.Tuples

colors = ("red","green","blue")

# Accessing items
"""
print(colors[0])
print(colors[1])
"""

# 3. Dictionaries

student = {
    "name": "Tanmay",
    "age": 21,
    "course": "Python"
}

# Access values
"""
print(student["name"])
"""

# Add new key
"""
student["city"] = "Pune"
print(student)
"""

#Modify Value
"""
student["age"] = 22
print(student)
"""

# Loop through Directory
"""
for key,value in student.items():
    print(key, value)
"""






















































































































































































