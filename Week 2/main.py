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
"""
Methods are functions that belong to a class.

They define the behaviour of objects created from class
"""
# Example
"""
class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("Hello, my name is "+ self.name)

p1 = Person("John")
p1.greet()
"""

# Methods with parameters
"""
methods can accept parameters like regular functions
"""

# Example
"""
class Calculator:
    def add(self,a,b):
        return a+b

    def multiply(self,a,b):
        return a*b

calc = Calculator()
print(calc.add(5,3))
print(calc.multiply(5,3))
"""

# Methods Accessing Properties
"""
Method can access and modify object properties using self
"""

# Example

"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

p1 = Person("Tobias",28)
print(p1.get_info())
"""

# Methods modifying Properties - methods can modify properties of object
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday! You are now {self.age}")

p1 = Person("Linus",25)
p1.celebrate_birthday()
p1.celebrate_birthday()
"""

# Multiple Methods - class can have that work together
"""
class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}' : ")
        for song in self.songs:
            print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Tension")
my_playlist.add_song("Guilty")
my_playlist.show_songs()
my_playlist.remove_song("Tension")
my_playlist.show_songs()
"""

# Delete Methods
"""
class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("Hello!")

p1 = Person("Linus")

p1.greet()

del Person.greet

p1.greet()  # this will throw error
"""

# Python Inheritance

"""
Inheritance allows us to define a class that inherits properties and 
methods from another class

Parent class - class being inherited from (also known as base class)
Child class - class that inherits (also known as derived class)
"""

# Create a Parent class
"""
class Parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)
"""

# child class
"""
class Student(Parent):
    pass

y = Student("Tanmay","Itape")
y.printname()
"""

# Types - Single, Multiple, MultiLevel, Hybrid,

# Single inheritance
"""
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


d1 = Dog()

d1.eat()
d1.bark()
"""












