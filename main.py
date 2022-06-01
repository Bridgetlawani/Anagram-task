import random


print("Welcome")
is_running = True



while is_running:
    print("Starting Game")
    choices = ["rock :R","paper:P", "scissors:S"]
    #player = input("rock, paper, or scissors \n")
    player = input("R,P or S \n")
    computer = random.choice(choices)

    try:
        
        #print(computer)
        while player in choices
        #print(player)    
        is_running = False

    except:
        player not in choices
        print("Invalid Input, Try Again!")
        continue

    if player == computer:
       print("computer: ",computer)
       print("player: ",player)
       print("Tie!")

    elif player == "rock":
        if computer == "paper":
           print("computer: ",computer)
           print("player: ",player)
           print("You lose!")

    elif player == "paper":
       if computer == "rock":
          print("computer: ",computer)
          print("player: ",player)
          print("You win")

    elif player == "scissors":
       if computer == "paper":
          print("computer: ",computer)
          print("player: ",player)
          print("You win!")

    elif player == "paper":
        if computer == "scissors":
          print("computer: ",computer)
          print("player: ",player)
          print("You lose!")

    elif player == "scissors":
        if computer == "rock":
          print("computer: ",computer)
          print("player: ",player)
          print("You lose!")

    elif player == "rock":
        if computer == "scisoors":
          print("computer: ",computer)
          print("player: ",player)
          print("You win!")

play_again = input("Would you like to play again? [yes/no]: ")
if play_again == "yes":
    is_running = True

if play_again == "no":
    print("Thank you for playing")
    is_running = False


