students = ["Dave", "John", "Bob"]

files = open("students.txt", "w")

for student in students:
    files.write(student + "\n")
    
files.close()
