import random

choices = ["rock", "paper","scissors"]

playerScore = 0
computScore = 0
computer = random.choice(choices)
player = None


while player not in choices:
    player = input("rock, paper, or scissors>: ").lower()
    if player == computer:
            print("the computer chooses: ",computer)
            print("the player chooses: ",player)
            print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("the computer chooses: ",computer)
            print("the player chooses: ",player)
            print("You lose!")
            computScore += 1 
        if computer == "scissor":
            print("the computer chooses: ",computer)
            print("the player chooses: ",player)
            print("You Win!")
            playerScore += 1
    elif player == "paper":
        if computer == "scissor":
            print("the computer chooses: ",computer)
            print("the player chooses: ",player)
            print("You lose!")
            computScore += 1
        if computer == "rock":
            print("the computer chooses: ",computer)
            print("the player chooses: ",player)
            print("You Win!")
            playerScore += 1
    elif player == "scissor":
        if computer == "rock":
            print("the computer chooses: ",computer)
            print("the player chooses: ",player)
            print("You lose!")
            computScore += 1
        if computer == "paper":
            print("the computer chooses: ",computer)
            print("the player chooses: ",player)
            print("You Win!")
            playerScore += 1
