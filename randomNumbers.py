import random

choices=["rock","paper","scissors"]

#boolean
isGameToBeContinued=True


while isGameToBeContinued:
    selection=input("what choice do you want, 1. rock, 2. paper, 3. scissors any other to quit")
    selectedChoice=selection.lower()

    #if you want to exit the game
    if selectedChoice not in choices:
        exit()

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
    elif selectedChoice=="rock" and computerChoice=="scissors":
        print("you have won")
    elif selectedChoice == "paper" and computerChoice == "paper":
        print("draw")
    elif selectedChoice == "paper" and computerChoice == "rock":
        print("You have lost")
    elif selectedChoice == "paper" and computerChoice == "scissors":
        print("you have won")
    elif selectedChoice == "scissors" and computerChoice == "scissors":
        print("draw")
    elif selectedChoice == "scissors" and computerChoice == "rock":
        print("You have lost")
    elif selectedChoice == "scissors" and computerChoice == "paper":
        print("you have won")






