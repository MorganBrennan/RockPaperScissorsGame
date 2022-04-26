import random

def playerInput():
    playerChoice = input("Rock, Paper, Scissors: ")
    lower = playerChoice.lower()
    return lower

def playAgain():
    again = input("Do you want to play again? ")
    if again == "yes":
        aiChoice()
    elif again == "no":
        exit

def aiChoice():
    lower = playerInput()
    
    rockPaperScissors = ["rock", "paper", "scissors"]

    if lower == "rock":
        chosen = random.choice(rockPaperScissors)
        if chosen == "rock":
            print("It's a tie!")
            playAgain()
        elif chosen == "paper":
            print("I win!")
            playAgain()
        elif chosen == "scissors":
            print("You win!")
            playAgain()
    elif lower == "paper":
        chosen = random.choice(rockPaperScissors)
        if chosen == "rock":
            print("You win!")
            playAgain()
        elif chosen == "scissors":
            print("I win!")
            playAgain()
        elif chosen == "paper":
            print("It's a tie!")
            playAgain()
    elif lower == "scissors":
        chosen = random.choice(rockPaperScissors)
        if chosen == "rock":
            print("You win!")
            playAgain()
        elif chosen == "paper":
            print("I win!")
            playAgain()
        elif chosen == "scissors":
            print("It's a tie!")
            playAgain()

def main():
    aiChoice()

main()