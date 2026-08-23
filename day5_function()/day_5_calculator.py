

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def ask_number():
    first_number = int(input("Enter first number:"))
    second_number = int(input("Enter second number:"))
    return first_number , second_number


def menu():
    print("\n1. Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.exit")
    choice = int(input("Enter your choice: "))
    return choice


calculator_on = True

while calculator_on:
    choice = menu()
    if choice >= 1 and choice <= 4:
        first_number, second_number = ask_number()
        if choice == 1:
            result = add(first_number, second_number)
            print("Addition:", result)
        elif choice == 2:
            result = subtract(first_number, second_number)
            print("Subtraction:", result)
        elif choice == 3:
            result = multiply(first_number, second_number)
            print("multiplication:", result)
        else:
            if second_number != 0:
                result = divide(first_number, second_number)
                print("Division:", result)
            else:
                print("Cannot divide by zero.")
    elif choice == 5:
            calculator_on = False
            print("calculator closed.")
    else:
        print("wrong input")
        
