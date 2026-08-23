class Student:
    def __init__(self, name, age,city,email):
        self.name = name
        self.age = age
        self.city=city
        self.email=email
    
    def __str__(self):
        return f"{self.name} - {self.age} - {self.city} - {self.email}"
        
    def display(self):
        print("---------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)
        print("Email:", self.email)
        
    def change_city(self, new_city):
        self.city = new_city
        print("City updated successfully.")
        
    def change_email(self,new_email):
        self.email = new_email
        print("Email updated successfully.")

def find_student(students, name):
    for student in students:
        if student.name == name:
            return student
    return None
students=[]




while True:
    while True:
        try:
            print("Student menu options:\n1.Add Student\n2.Show Student\n3.Update City\n4.Delete student\n5.Update Email\n6.Found Student\n7.Display all student\n8.Exit")
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter valid input.")
        else:
            break 
    if choice == 1:
        name = input("Enter student name: ")
        while True:
            try:
                age = int(input("Enter age: "))
            except ValueError:
                print("Enter valid input.")
            else:
                break
        city = input("Enter city: ")
        email = input("Enter email: ")
        new_student = Student(name, age, city, email)
        students.append(new_student)
        print("Student added.")
        
        
    elif choice == 2:
        for student in students:
            student.display()
            
            
    elif choice == 3:
        name1 = input("Enter student name: ")
        student = find_student(students, name1)

        if student is not None:
            student.change_city(input("Enter new city: "))
        else:
            print("Student is not found.")
            
            
    elif choice==4:
        name2=input("Enter student name to delete:")
        
        student_del=find_student(students,name2)
        
        if student_del is not None:
            students.remove(student_del)
            print("Student removed")
        else:
            print("Student is not found.")
            
    elif choice == 5:
        name2 = input("Enter student name: ")
        student = find_student(students, name2)
        
        if student is not None:
            student.change_email(input("Enter new email: "))
                
        else:
            print("Student not found.")
    
    elif choice ==6 :
        name3 = input("Enter student name: ")
        student = find_student(students, name3)
        
        if student is not None:
            student.display()
                        
        else:
            print("Student not found.")
            
    elif choice==7:
        for student in students:
            print(student) 
    elif choice == 8:
        print("Good bye.")
        break
        
    else:
        print("Wrong input.")

