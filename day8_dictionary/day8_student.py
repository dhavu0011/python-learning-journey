def show_student(student):
    for key, value in student.items():
        print(key, ":", value)


def update_record_student(student, field):
    updated_data = input(f"Enter new {field}: ")
    student[field] = updated_data
    print(f"{field.capitalize()} updated.")

    
def show_field(student, field):
    print(f"{field.capitalize()}: {student[field]}")


student = {
    "name":"Dave",
    "age":25,
    "city":"Warren",
    "email":"dave@yahoo.com"
}

while True:
    print("Student menu options:\n1.Show Student\n2.Update City\n3.Update Email\n4.Show Only Email\n5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        show_student(student)
    elif choice == 2:
        update_record_student(student, "city")
    elif choice == 3:
        update_record_student(student, "email")
    elif choice == 4:
        show_field(student, "email")
    elif choice == 5:
        print("Good bye.")
        break
        
    else:
        print("Wrong input.")
        
