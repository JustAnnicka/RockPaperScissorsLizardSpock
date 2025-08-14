import random
import assets

game_images = [assets.rock, assets.paper, assets.scissors, assets.lizard, assets.spock]
print("Welcome to the Rock-Paper-Scissors-Lizard-Spock game")
#add Rules input choice type H for help
# add input for rounds to be played (best of 5) (draws dont count?) or if equal then do a golden game (with repeat on draw)
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
elif (user_choice > computer_choice or (user_choice == 0 and computer_choice == 2)
    or user_choice == 2 and computer_choice == 3 or user_choice == 1 and computer_choice == 4):
    print("you win")
else:
    print("you loose")

#Add score printing
