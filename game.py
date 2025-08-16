import random
import assets

game_images = [assets.rock, assets.paper, assets.scissors, assets.lizard, assets.spock]
print("Welcome to the Rock-Paper-Scissors-Lizard-Spock game")
if input("If you are'nt familiar with the rules tupe 'R', or just start the game with enter\n").lower() == "r":
    print(assets.rules)

rounds = int(input("How many rounds would you like to play. (best of [nbr] principle). Type a number to set\n")) #nbr check this for proper input
user_score = 0
computer_score = 0
for i in range(0, rounds):
    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard or 4 for Spock\n")
    computer_choice = random.randint(0,4)
    while user_choice != "0" and user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4":
        user_choice = input("That\'s not a valid please type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard or 4 for Spock\n")
    user_choice = int(user_choice)
    print("your choice" + game_images[user_choice] + "\nComputer chose\n" + game_images[computer_choice])
    if user_choice == computer_choice:
        print("That's a draw")
    elif (computer_choice == 0 and (user_choice == 2 or user_choice == 3)
        or computer_choice == 3 and (user_choice == 2 or user_choice == 4)
        or computer_choice == 4 and user_choice == 2): #do I need to check for the higher one? as should be handled by the else
        print("you loose")
        computer_score += 1
    elif (user_choice > computer_choice or (user_choice == 0 and computer_choice == 2)
        or user_choice == 2 and computer_choice == 3 or user_choice == 1 and computer_choice == 4):
        print("you win")
        user_score += 1
    else:
        print("you loose")
        computer_score += 1
    print(f"computer: {computer_score}, user: {user_score}")
if computer_score > user_score:
    print("Computer won! Better luck next time.")
elif computer_score < user_score:
    print("You won! Great Job!")
else:
    print("Ohh thats a draw. Go play again")

