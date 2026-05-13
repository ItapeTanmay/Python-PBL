from pathlib import Path   # Path tool to handle files and folders

file_path = Path("notes.txt")  # We created Path object so now python knows we are working with notes.txt

# writing the file
"""
file_path.write_text("Hello, This is my first text")
"""

# write_text overwrites the file
"""
file_path.write_text("Hey")
"""

# Reading the contents of file
"""
content = file_path.read_text()
print(content)
"""

# Append data
"""
with file_path.open("a") as file:
    file.write("\nLearning File I/O")
"""

# read file

with file_path.open("r") as file:
    for line in file:
        print(line.strip())  # we use strip to remove extra gaps we had due to \n.



