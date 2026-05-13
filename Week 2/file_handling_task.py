from pathlib import Path

file_path = Path("Practice.txt")

note = input("Enter input: ")

with file_path.open("a") as file:
    file.write(note+"\n")

count = 1
with file_path.open("r") as file:
    for line in file:
        print(count,".",line.strip())
        count += 1