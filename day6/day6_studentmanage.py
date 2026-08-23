def student_menu():
    print("\n 1.Show Students \n2.Add Students \n3.Remove Student \n4.Exit")
    choice = int(input("\nEnter what would you like to do:"))
    return choice


def student_show(students):
    print("\nStudent list:")
    for student in students:
        print(student)


def add_student(students):
    name = input("\nenter the name:")
    students.append(name)

    
def remove_student(students):
    name = input("Enter student name to remove: ")

    if name in students:
        students.remove(name)
        print("Student removed.")
    else:
        print("Student not found.")


student_menu_open = True
students = ["Dave", "John", "Bob"]

while student_menu_open:
    choice = student_menu()
    if 1 <= choice <= 4:
        if choice == 1:
            student_show(students)
        elif choice == 2:
            add_student(students)
            print("Student added.")
        elif choice == 3:
            remove_student(students)
            
        else:
            print("Goodbye..")
            break
    else:
        print("Wrong input")        
    
