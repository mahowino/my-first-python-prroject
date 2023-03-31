import random


print("player 1")
# Choose a random word
word = input("choose the word to play with")

# Initialize guesses
guesses = ''

# Set the number of turns
turns = 10

# Loop until turns run out or the word is guessed
while turns > 0:

    # Keep track of whether the word has been guessed
    guessed = True

    # Print the current state of the word
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            guessed = False

    # If the word has been guessed, end the game
    if guessed:
        print('\nCongratulations, you guessed the word!')
        break

    # Ask the user for a guess
    guess = input('\nGuess a letter: ')

    # Add the guess to the list of guesses
    guesses += guess

    # Decrement the number of turns if the guess is incorrect
    if guess not in word:
        turns -= 1
        print(f'Incorrect. You have {turns} turns left.')

    # If the guess is correct, inform the user
    else:
        print('Correct!')

# If the loop ends without guessing the word, end the game and reveal the word
else:
    print(f'Sorry, you ran out of turns. The word was "{word}".')

# End of the game
print('Thanks for playing!')