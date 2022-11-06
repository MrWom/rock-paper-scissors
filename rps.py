import random

choiceList = ["Rock", "Paper", "Scissors"]

def main():
    print("Hello there welcome to my quick version of Rock, paper, scicssors!")
    print("How many rounds would you like to play?")
    print("1 Rounds | 3 Rounds | 5 Rounds")
    print("")
    game()

#Asks user if they wish to play again on win
def win():
    print("Congrats you have won!")
    print("")
    print("Want to play again? (y/n)")
    theEnd = input()
    if theEnd == "y":
        main()
    else:
        quit()
#Asks user if they wish to play again on loss
def lose():
    print("You have lost D:")
    print("")
    print("Want to play again? (y/n)")
    theEnd = input()
    if theEnd == "y":
        main()
    else:
        quit()

def game():
    numRounds = int(input("Number of Rounds: "))
    counter = numRounds
    aiPoints = 0
    playerPoints = 0
    while counter > 0:
        aiChoice = random.choice(choiceList)
        print("")
        print("Player Score: " + str(playerPoints) + " | AI Points: " + str(aiPoints))
        print("")
        if numRounds == 1:
            print("Rock, Paper or Scicssors?")
            playerChoice = str(input())
            print("The AI has chosen " + aiChoice)
            print("")

            if playerChoice == aiChoice:
                print("This round is a draw!")

            elif aiChoice == "Rock":
                if playerChoice == "Paper":
                    print("You win this round!")
                    counter = counter - 1
                    playerPoints = playerPoints + 1

                else:
                    print("You lose this round")
                    counter = counter - 1
                    aiPoints = aiPoints + 1


            elif aiChoice == "Paper":
                if playerChoice == "Scissors":
                    print("You win this round!")
                    counter = counter - 1
                    playerPoints = playerPoints + 1

                else:
                    print("You lose this round")
                    counter = counter - 1
                    aiPoints = aiPoints + 1


            elif aiChoice == "Scissors":
                if playerChoice == "Rock":
                    print("You win this round!")
                    counter = counter - 1
                    playerPoints = playerPoints + 1

                else:
                    print("You lose this round")
                    counter = counter - 1
                    aiPoints = aiPoints + 1

        elif numRounds == 3:
            print("Rock, Paper or Scicssors?")
            playerChoice = str(input())
            print("The AI has chosen " + aiChoice)
            print("")

            if playerChoice == aiChoice:
                print("This round is a draw!")

            elif aiChoice == "Rock":
                if playerChoice == "Paper":
                    print("You win this round!")
                    counter = counter - 1
                    playerPoints = playerPoints + 1

                else:
                    print("You lose this round")
                    counter = counter - 1
                    aiPoints = aiPoints + 1


            elif aiChoice == "Paper":
                if playerChoice == "Scissors":
                    print("You win this round!")
                    counter = counter - 1
                    playerPoints = playerPoints + 1

                else:
                    print("You lose this round")
                    counter = counter - 1
                    aiPoints = aiPoints + 1


            elif aiChoice == "Scissors":
                if playerChoice == "Rock":
                    print("You win this round!")
                    counter = counter - 1
                    playerPoints = playerPoints + 1

                else:
                    print("You lose this round")
                    counter = counter - 1
                    aiPoints = aiPoints + 1

        elif numRounds == 5:
            print("Rock, Paper or Scicssors?")
            playerChoice = str(input())
            print("The AI has chosen " + aiChoice)
            print("")

            if playerChoice == aiChoice:
                print("This round is a draw!")

            elif aiChoice == "Rock":
                if playerChoice == "Paper":
                    print("You win this round!")
                    counter = counter - 1
                    playerPoints = playerPoints + 1

                else:
                    print("You lose this round")
                    counter = counter - 1
                    aiPoints = aiPoints + 1


            elif aiChoice == "Paper":
                if playerChoice == "Scissors":
                    print("You win this round!")
                    counter = counter - 1
                    playerPoints = playerPoints + 1

                else:
                    print("You lose this round")
                    counter = counter - 1
                    aiPoints = aiPoints + 1


            elif aiChoice == "Scissors":
                if playerChoice == "Rock":
                    print("You win this round!")
                    counter = counter - 1
                    playerPoints = playerPoints + 1

                else:
                    print("You lose this round")
                    counter = counter - 1
                    aiPoints = aiPoints + 1
                    
    if playerPoints > aiPoints:
        print("Player Score: " + str(playerPoints) + " | AI Points: " + str(aiPoints))
        win()
    else:
        print("Player Score: " + str(playerPoints) + " | AI Points: " + str(aiPoints))
        lose()

main()
