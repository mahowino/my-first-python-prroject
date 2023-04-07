import random


randomLowerBound=random.randint(0,10)
randomUpperBound=random.randint(randomLowerBound,10)
selectedRandomNuber=random.randint(randomLowerBound,randomUpperBound)

print("guessing game")
guessedNumber=int(input("guess a number between "+str(randomLowerBound)+" and"+str(randomUpperBound)))

if(selectedRandomNuber == guessedNumber):
    print("you have gotten it")
else:
    print("failed")
    print("the guessed number was",guessedNumber)
print("the computer number was",selectedRandomNuber)
