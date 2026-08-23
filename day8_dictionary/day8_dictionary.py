student = { 
        "name":"Dave",
        "age":25,
        "city":"Warren"}

student["email"] = "dave@yaahoo.com"
print(student)

for key, value in student.items():
    print(key, ":", value)

if "age" in student:
    print("age exists.")

book = {
    "title":"Python Basics",
    "author":"Dave",
    "pages":300
}

print(f"Title is: {book['title']}")
print("Author is ", book["author"])

car = {
    "brand":"Toyota",
    "year":2022
}

car["color"] = "red"
car["year"] = 2024
print(car)

student = {
    "name":"Dave"
}

print(student["city"])
