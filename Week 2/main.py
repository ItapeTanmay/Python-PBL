# Topic 1 : OOP (Object Oriented Programming)

# Class - A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
    x = 5

# Object
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

P1 = MyClass()
P2 = MyClass()
P3 = MyClass()

print(P1.x)
print(P2.x)
print(P3.x)

# Pass - If class is empty for some reason, you add Pass into it

class Person:
    pass

# __init__() Method
