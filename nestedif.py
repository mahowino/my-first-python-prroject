#you have a game which has a difficulty of 10
#print a different message if the game is running and the difficulty is 10

isGameRunning=True
difficulty=11
playerLevel=12

if isGameRunning==True:
    if difficulty>10:
        print("this game is hard")
        if playerLevel>=20:
            print("hi")
        else:
            print("not hi")
    else:
        print("this game is easy")
else:
    print("game is not running")


if difficulty==10:
    print("difficulty is 10")
else: print("difficulty is not 10")

print("difficulty is 10") if difficulty==10 else print("difficulty is not 10")