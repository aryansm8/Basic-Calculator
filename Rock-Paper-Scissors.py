#Rock, Paper, and Scissors:

import random

Wins = 0
Losses = 0
Ties = 0

user_input = input("Would you like to play Rock, Paper, Scissors?")

print ("R for Rock")
print ("P for Paper")
print ("S for Scissors")


#Determining user input, and commanding computer selection.
while True:
    possible_choices = ["Rock", "Paper", "Scissors",]
    possible_choices = ["Rock", "Paper", "Scissors"]
    user_choice = input("Please select Rock, Paper or Scissors:")
    computer_choice = random.choice (possible_choices)
    if user_choice not in possible_choices:
        print = input("Enter a valid choice.")
        continue
    print ("Play!")
    print ("You chose", (user_choice), "and the computer chose", (computer_choice))

#Possible outcomes
#Outcome 1
    if user_choice == computer_choice:
        print ("It's a Tie!")
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print ("You Lose!")
            Losses + 1
        else:
            print ("You Win")
            Wins + 1
            break

#Outcome 2

    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print ("You Win")
            Wins + 1
        else:
            print ("You Lose")
            Losses + 1
            break

    elif user_choice == "Scissors":
        if computer_choice == "Rock":
                print ("You Lose!")
                Losses + 1
        
        else:
            print ("You Win")
            Wins + 1
            break

#Outcome 3

    elif user_choice == "Paper":
        if computer_choice == "Scissors":
                print ("You Lose!")
                Losses + 1
                break

        else:
            print ("You Win")
            Wins + 1
            break


