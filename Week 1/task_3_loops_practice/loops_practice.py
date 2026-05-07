# Task 1 - Prints numbers 1 to 10

for num in range(1,11):
    print(num)

# Task 2 - Name Repeater - repeat names for 5 times

name = input("Enter your name: ")
count = 1
while count <= 5:
    print(f"hello {name}")
    count += 1

# Task 3 - print multiplication table

num = int(input("Enter the number you want table of: "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

# Task 4 - while Loop Countdown

timer = int(input("enter number to start countdown"))
while timer>=1:
    print(timer)
    timer -= 1
print("Blast off")

# Task 5 - Asking password until user gives it right

og_password = "python123"
user_pass = input("enter your pass")

while user_pass != og_password:
    print("You entered wrong password: ")
    user_pass = input("enter your pass")

print("Access granted")


