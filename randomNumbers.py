import random

choices=["rock","paper","scissors"]

#boolean
isGameToBeContinued=True
compScore=0
userScore=0


while isGameToBeContinued:
    selection=input("what choice do you want, 1. rock, 2. paper, 3. scissors any other to quit")
    selectedChoice=selection.lower()

    #if you want to exit the game
    if selectedChoice not in choices:
        break

    #make the computer make a selection
    selectedIndex=random.randint(0,2)
    computerChoice=choices[selectedIndex]

    # gives us the results
    print("computer choice was " + computerChoice)
    print("your choice was " + selectedChoice)

    if selectedChoice=="rock" and computerChoice=="rock":
        print("draw")
    elif selectedChoice=="rock" and computerChoice=="paper":
        print("You have lost")
        compScore+=1
    elif selectedChoice=="rock" and computerChoice=="scissors":
        print("you have won")
        userScore+=1
    elif selectedChoice == "paper" and computerChoice == "paper":
        print("draw")
    elif selectedChoice == "paper" and computerChoice == "rock":
        print("You have won")
        userScore +=1

    elif selectedChoice == "paper" and computerChoice == "scissors":
        print("you have won")
        compScore += 1

    elif selectedChoice == "scissors" and computerChoice == "scissors":
        print("draw")
    elif selectedChoice == "scissors" and computerChoice == "rock":
        print("You have lost")
        compScore += 1
    elif selectedChoice == "scissors" and computerChoice == "paper":
        print("you have won")
        userScore += 1

    print("user score is ",userScore)
    print("comp score is ",compScore)

    if userScore==5 or compScore ==5:
        if compScore==5:
            print("computer wins")
        else:
            print("user wins")
        break





