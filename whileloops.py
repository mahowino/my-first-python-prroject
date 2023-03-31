


def printSquares(number):
    square = number * number
    print(square)


isInputGiven = True
global n

while isInputGiven:
    x=input("what is the range in which you want to square?")

    if x != "":
        n=int(x)
        isInputGiven = False


printSquares(n)
