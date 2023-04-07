import random
#rock paper scissors

continue_game=True
choices=["rock","paper","scissors"]
while continue_game:
    selection=input("choose a selection, rock, paper or scissors?, any other to quit").lower()

    if selection not in choices:
        exit()
    selectedIndex=random.randint(0,2)
    selectedText=choices[selectedIndex]

    if selection=="rock" and selectedText=="paper":
        print("you loose")
        print(selection)
        print(selectedText)
    else:
        print("you win")
        print(selection)
        print(selectedText)






print(random.randint(0,4))