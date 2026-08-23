

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    
    except ZeroDivisionError:
        return None


def ask_number():
    while True:
        try:
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))

        except ValueError:
            print("Invalid input. Please enter numbers only.")
        
        else:
            return first_number, second_number


def menu():
    while True:
        try:
            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            choice = int(input("Enter your choice: "))
            
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please choose between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")


calculator_on = True

while calculator_on:
    choice = menu()

    if 1 <= choice <= 4:
        first_number, second_number = ask_number()

        if choice == 1:
            print("Addition:", add(first_number, second_number))

        elif choice == 2:
            print("Subtraction:", subtract(first_number, second_number))

        elif choice == 3:
            print("Multiplication:", multiply(first_number, second_number))

        else:
            result = divide(first_number, second_number)
            if result is None:
                print("Cannot divide by zero.")
            else:
                print("Division:", result)
    elif choice == 5:
        print("Calculator closed.")
        calculator_on = False

    else:
        print("Wrong menu choice.")

