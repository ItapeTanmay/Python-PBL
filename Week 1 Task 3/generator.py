# Difference between Iterator, Iterables and Iteration
"""
1.Iterables - An object that gives us iterator method
2.Iterator - object that has __next__() method
3.Iteration - fetching next item in iterable list
"""

# Generator

"""
1. Functions that can pause and resume their execution
2. when generator function is called, it generates a generator object, which is an iterator
3. the code inside the function is not executed it is only compiled.
4. It only executes when you iterate over a generator
"""

"""
Main highlight of generator is it allows you to iterator over data without storing 
the entire dataset into your memory 
"""

"""
Instead of using return, generators use yield keyword
"""

# A simple Generator example
"""
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)
"""

# yield keyword
"""
1.The yield keyword is what makes a function a generator.
2.When yield is encountered, the function's state is saved, and the value is returned. 
  The next time the generator is called, it continues from where it left off.
"""

# Example
"""
def count_up_to(n):
    count = 1
    while count < n:
        yield count
        count +=1

for num in count_up_to(5):
    print(num)
"""

# Generators Save memory
"""
1.Generators are memory efficient because they generate values on-the fly and 
  do not store in memory
2. For large datasets it is very useful
"""

# Example
"""
def large_sequence(n):
    for i in range(n):
        yield i

# This does not create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))  # we can use next() to manually iterate through generator
print(next(gen))
print(next(gen))
"""

# StopIteration
"""
When no more values to yield, generator raises a StopIteration exception
"""

# Example
"""
def simple_gen():
    yield 1
    yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
#print(next(gen))  this will raise StopIteration
"""

# Generator expressions

#Example
"""
# List comprehension - creates a list
list_comp = [x*x for x in range(5)]
print(list_comp)

# Generator comprehension - creates a generator
gen_exp = (x*x for x in range(5))
print(gen_exp)
print(list(gen_exp))
"""

# Example - Using generator expression with sum
"""
# calculate sum of squares without creating a list
total = sum(x*x for x in range(10))
print(total)
"""

# Fibonacci sequencer Generator
"""
def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

# get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
    print(next(gen))
"""

# Generator Methods - generators have special methods for advanced control

# 1. send() method - allows you to send a value to the generator

# Example
"""
def echo_generator():
    while True:
        received = yield
        print("received:", received)

gen = echo_generator()
next(gen) # starting the generator
gen.send("Hello")
gen.send("World")
"""

# 2. close() method - it stops the generator

# example
def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")

gen = my_gen()
print(next(gen))
print(next(gen))
gen.close()






























































































