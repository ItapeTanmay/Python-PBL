# Task 1 : Greet User Function

def greet_user(name):
    print(f"Hello {name}, welcome to python")

# greet_user("Tanmay")

# Task 2 : Grade Function

def check_grade(marks):
    if marks >= 90:
        return "A Grade"
    elif marks >= 75:
        return "B Grade"
    elif marks >= 50:
        return "C Grade"
    else:
        return "Fail"

# print(check_grade(95))

# Task 1 : Multiplication Table Function

def multiplication_table(num):
    for i in range(1,11):
        print(f"{num}X{i} = {num*i}")

# multiplication_table(3)





