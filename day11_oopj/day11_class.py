class Studento:
    def __init__(self, name, age,city,email):
        self.name = name
        self.age = age
        self.city=city
        self.email=email


student1 = Studento("Dave", 25,"warren","ddd@gmail.com")
student2 = Studento("Bob", 20,"kane","ppp@gmail.com")

print(student1.name)
print(student2.name)
print(student1.email)

class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year=year
        
car1= Car("honda",2024)
car2= Car("jeep",2023)

print(car1.brand)
print(car2.brand)

class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        
book1=book("python","chatgpt")

print(book1.author)
print(book1.title)        
