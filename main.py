"""
Cows and Bulls

A simple text based game for two people. Player 1 thinks of a hidden word and Player 2 tries to guess.
Each guess by P2 is given a score by P1 so - for each letter in the guess, if it is present in the hidden word but is in
the wrong position, it counts as a Cow. If it is in the correct position too, it instead counts as a Bull.
Thus, if the hidden word is BLUE and the guess word is BALE, ths score for this guess would be Cows - 1, Bulls - 2
    ^ 1 for Cows because L is present in both the guess and the hidden word, but is not in the correct position in the guess
    ^ 2 for Bulls because B and E are present in both and in the correct position.

As P2 keeps guessing, more information about the hidden word is revealed, aiding P2 in getting closer to the hidden word.

Two simple rules to be followed though - the length of the guess word must be the same as the length of the hidden word and
the hidden word cannot have the same letter more than once i.e. BULK is an acceptable hidden word but BULL is not, because it
has more than one of the same letter.
"""

import getpass
import pandas as pd

#Take word input from user 1word

def runGame():
    """
    Basic flow of the game - 
        1. Enter hidden word. This is the word to be guessed.
        2. Enter a guess. This will be scored as per the scoring logic.
        3. Use the Cows and Bulls of previous guess to make the next guess.
    """
    print("Enter the hidden word. Remember, no repeated characters in it.")
    print("(Don't worry, the hidden word will not show up when you type it here)")
    hiddenWord = getpass.getpass("")


    """Check if the given hidden word has repeated characters. If it does, take input again"""
    while len(set(hiddenWord)) != len(hiddenWord):
        print("Word with repeated letters not allowed. Enter again.")
        hiddenWord = getpass.getpass("")

    
    print("Start guessing")
    cols = ["Attempt word", "Cows", "Bulls"]
    scoreKeeper = pd.DataFrame(columns=cols)
    length = len(hiddenWord)
    print("Length of hidden word-", length)
    counter = 0

    while True:
        cows = 0
        bulls = 0
        guessWord = input("Make a guess - ")
        print()
        
        """To ensure that the lengths of hidden word and guess word are the same"""
        if len(guessWord)!=length:
            print("Incorrect length of guess word. Try again.")
            continue
        
        i = 0
        """Count the number of Bulls"""
        while i < length:
            if hiddenWord[i] == guessWord[i]:
                bulls += 1
            i += 1
        
        i = 0
        """Count the number of Cows"""
        while i < length:
            if hiddenWord[i] in guessWord and hiddenWord[i] != guessWord[i]:
                cows += 1
            i += 1


        scoreKeeper.loc[counter] = [guessWord,cows,bulls]
        print(scoreKeeper,"\n")
        if bulls == length and guessWord == hiddenWord:
            print("Success! You guessed the word ",hiddenWord.upper())
            break
        counter += 1


if __name__=="__main__":
    runGame()