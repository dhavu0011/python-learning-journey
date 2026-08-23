try:
    number = int(input("Enter value: "))
    print(number)

except ValueError:
    print("invalid number.")

try:
    number = int(input("Enter number: "))
    divide = 100 / number

    print(divide)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Answer:", divide)

try:
    age = int(input("Age: "))

except ValueError:
    print("Invalid age.")

else:
    print("Age entered successfully.")
