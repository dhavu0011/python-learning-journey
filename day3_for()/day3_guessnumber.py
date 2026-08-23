secret = 7
number = int(input("Guess the number:"))
if number == secret:
    print("Congratulations! You guessed correctly.")
elif number < secret:
    print("The number is too low.")
else:
    print("The number is too high")
    
answer = input("Do you want to play again ? (y/n):").lower()
if answer == "n":
    print("Thanks for playing!")
elif answer == "y":
    print("Great! We'll play again tomorrow.")
else:
    print("Enter valid input.")

