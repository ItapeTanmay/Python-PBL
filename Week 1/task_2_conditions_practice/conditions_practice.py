name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

has_id = True
is_banned = False

if age >= 18 and has_id and not is_banned:
    print(f"{name}, You are eligible for the event")
else:
    print(f"{name}, You are not eligible for this event")

if marks>=90:
    print(f"{name}, You got A Grade")
elif marks>=75:
    print(f"{name}, You got B Grade")
elif marks>=50:
    print(f"{name}, You got C Grade")
else:
    print(f"{name}, you have failed")
