game_started = False
game_run = True

while game_run:
    menu = int(input("\n1. Start Game \n 2. Settings \n 3. Exit \n enter your choice: "))
    if menu == 1:
        if not game_started:
            print("Staring game...")
            game_started = True
        else:
            print("Game already started.")
    elif menu == 2:
        print("Opening Settings....")
    elif menu == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
    
