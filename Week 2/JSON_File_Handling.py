from pathlib import Path
import json

file_path = Path("student.json")

"""
student_data = {
    "name" : "John",
    "age" : "21",
    "course" : "Computer Science"
}

with file_path.open("w") as file:
    json.dump(student_data,file,indent=4)   # json.dump() writes JSON data

data = {
    "name" : "Tanmay",
    "skills" : ["Python","CEH","CHFI"],
    "CGPA" : 8.5
}

with file_path.open("w") as file:
    json.dump(data,file,indent=4)

with file_path.open("r") as file:
    details = json.load(file)

print("name",data["name"])
print("CGPA",data["CGPA"])
print("Skills")
for skill in data["skills"]:
    print(skill)
"""

# Multiple Inputs
students = [
    {
        "name": "Tanmay",
        "CGPA": 8.5,
        "skills": ["Python", "CEH"]
    },
    {
        "name": "Rahul",
        "CGPA": 7.9,
        "skills": ["Java", "SQL"]
    }
]

with file_path.open("w") as file:
    json.dump(students, file, indent=4)

# Read multiple inputs

"""

with file_path.open("r") as file:
    students = json.load(file)

print(students)

with file_path.open("r") as file:
    for student in students:
        print(student["name"])
"""

# take user input to add into existing data
"""
# Import json module to work with JSON files
import json


# Open the JSON file in read mode and load existing data
with open("students.json", "r") as file:
    data = json.load(file)


# Take new student details from user
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))


# Create a dictionary for new student data
new_student = {
    "name": name,
    "roll_no": roll_no
}


# Add new student dictionary into existing list
data.append(new_student)


# Open the same file in write mode to update data
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)


# Print success message
print("Student added successfully!")
"""

