# Topic 1 : OOP (Object Oriented Programming)

# Class - A Class is like an object constructor, or a "blueprint" for creating objects.
"""
class MyClass:
    x = 5
"""

# Object - Instance of Class
"""
P1 = MyClass()
print(P1.x)
"""

# Delete Object
"""
del P1
print(P1.x)
"""

# Multiple Objects
"""
P1 = MyClass()
P2 = MyClass()
P3 = MyClass()

print(P1.x)
print(P2.x)
print(P3.x)
"""

# Pass - If class is empty for some reason, you add Pass into it
"""
class Person:
    pass
"""

# __init__() Method - In built method that being initiated in start
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Emily",36)

print(p1.name)
print(p1.age)
"""

# Why __init__() ?
"""
Because without __init__() We need to set properties manually for each 
object
"""

# Example
"""
class Person:
    pass

P1 = Person()
P1.name = "John"
P1.age = 23

print(P1.name)
print(P1.age)
"""

# Default values in __init__()
"""
class Person:
    def __init__(self,name,age = 18):
        self.name = name
        self.age = age

p1 = Person("Emily") 
p2 = Person("John",23)

print(p1.name,p1.age) # p1.age will print 18 as it is by default value
print(p2.name,p2.age)
"""

# Multiple Parameters - __init__() can have as many parameters as you need
"""
class Person:
    def __init__(self,name,age,city,country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Emily",24,"Pune","India")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
"""

# Python Self parameter
"""
The self parameter is a reference to the current instance of the class

It is used to access properties and methods that belong to the class
"""

# Example
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, My name is "+self.name)

p1 = Person("John",25)
p1.greet()
"""

# Why use self ?

"""
Without self, Python would not know which object's properties
you want to access
"""

# self does not Have to be named "Self"
"""
class Person:
    def __init__(myobject,name,age):
        myobject.name = name
        myobject.age = age

    def greet(abc):
        print("Hello, My name is "+abc.name)

p1 = Person("john",25)
p1.greet()
"""

# Accessing properties with self
"""
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota","corolla",2020)
car1.display_info()
"""

# calling methods using self
"""
class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        return "Hello, "+ self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website")

p1 = Person("John")
p1.welcome()
"""

# Python Class Properties
"""
Properties are variables that belong to a class.

They store data for each object created from the class
"""

# Example
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("John",36)
print(p1.name)
print(p1.age)
"""

# Access Properties - Can access properties using dot notation
"""
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota","Corolla")
print(car1.brand,car1.model)
"""

# Modify Properties - can modify value of properties
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("John",25)
print(p1.age)

p1.age = 36
print(p1.age)
"""

# Delete Properties - can delete properties using del keyword
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 =Person("John",45)
print(p1.age)

del p1.age

print(p1.name) # this works
# print(p1.age) # this will not work
"""

# class Property vs Object Property
"""
class Person:
    species = "Human"  # class property

    def __init__(self,name):
        self.name = name   # instance prorerty

p1 = Person("Emil")
p2 = Person("John")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
"""

# modifying class Properties

"""
When you modify class property it affects all objects
"""

# Example
"""
class Person:
    lastname = "Gaviria"

    def __init__(self,name):
        self.name = name

p1 = Person("Emily")
p2 = Person("John")
print(p1.name,p1.lastname)
print(p2.name,p2.lastname)

Person.lastname = "Linus"
print(p1.name,p1.lastname)
print(p2.name,p2.lastname)
"""

# Add new properties
"""
class Person:
    def __init__(self,name):
        self.name = name

p1 = Person("Tobias")
p1.age = 25
p1.city = "olso"

print(p1.name,p1.age,p1.city)
"""

"""
Adding property this way only adds to that specific object,
not to all objects of the class
"""

# Class Methods


















