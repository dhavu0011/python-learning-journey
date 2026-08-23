def student_show(students):
    print("\nStudent list:")
    for student in students:
        print(student)

        
def add_student(students):
    name = input("\nenter the name:")
    students.append(name)
    print("Student Added.")


def remove_student(students):
    name = input("Enter student name to remove: ")

    if name in students:
        students.remove(name)
        print("Student removed.")
    else:
        print("Student not found.")

    
def search_student(students):
    name = input("Enter student name: ")

    if name in students:
        print("Student Found.")
    else:
        print("Student not found.")


def change_student_name(students):
    old_name = input("Enter old name: ")
    if old_name in students:
        new_name = input("Enter New name: ")
        index = students.index(old_name)
        students[index] = new_name
        print("Student name changed.")
    else:
        print("Student not found")


def student_count(students):
    count = len(students)
    print("Total students: ", count)


def save_students(students):
    with open("students.txt", "w") as file:
        for student in students:
            file.write(student + "\n")
            
    print("Students saved successfully")


def load_students():
    students = []
    with open("students.txt", "r") as file:
        for line in file:
            students.append(line.strip())
    return students


def clear_students(students):
    students.clear()


students = ["Dave", "Bob"]

while True:
    print("\nStudent management options: \n1.Show Students \n2.Add Student \n3.Remove Student \n4.Search Student \n5.Update Student \n6.Count Students \n7.Save Students \n8.Load Students \n9.Exit \n10.clear all student")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        student_show(students)    
    elif choice == 2:
        add_student(students)
    elif choice == 3:
        remove_student(students)
    elif choice == 4:
        search_student(students)
    elif choice == 5:
        change_student_name(students)
    elif choice == 6:
        student_count(students)
    elif choice == 7:
        save_students(students)
    elif choice == 8:
        load_students()
        print("Students loaded successfully.")
    elif choice == 9:
        print("Goodbye")
        break
    elif choice == 10:
        choose = input("Are you sure? (y/n):")
        if choose == "y":
            clear_students(students)
            print("All students removed.")
        elif choose == "n":
            print("Operation cancelled.")
        else:
            print("Wrong input.")
    else:
        print("Wrong input.")

