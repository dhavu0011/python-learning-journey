secret = 7
game_running = True

while game_running:
    number = int(input("Guess the number:"))
    if number == secret:
        print("Congratulations! You guessed correctly.")
        answer = input("Do you want to play again ? (y/n):").lower()
        if answer == "n":
            print("Thanks for playing!")
            break
        elif answer == "y":
            print("Great! We'll play again.")
        else:
            print("Enter valid input.")
    elif number < secret:
        print("The number is too low.")
    else:
        print("The number is too high")

