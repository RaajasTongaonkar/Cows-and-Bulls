# Cows-and-Bulls
A (very) simple implementation of the text based game Cows &amp; Bulls

## Execution
Run try.py file. You'll need Pandas and Getpass libraries - Pandas purely for displaying the scores and Getpass for hiding the source word.

## The Game
This is a simple text matching game. Player one(P1) selects one word(source word), and player two(P2) has to guess it. 
Usually there is no limit on the number of turns P2 gets to guess the word but it's up to the players. The game is over when P2 guesses the word correctly.
Cows and bulls refers to the two scores for each guessword that are generated. Both are numeric. A score under Cows refers to how many letters in the guessword are present in the source word, but are in the wrong place. A score under Bulls refers to how many letters in the guessword are present in the source word *and* are in the correct position.

Eg - 
 Suppose the source word is REST and the first guessword is STAR. Then the scores will look like this - 
      Cows|Bulls
  STAR  3   0
 This is because STAR has three letters (S, T, R) that are present in REST, but none of them are in the correct position, thus 3 under      Cows.
 Now suppose the guessword is ROBE. Then the scores will be -
      Cows|Bulls
  ROBE  1   1
 The 1 under Bulls is for the R, which is in the source word and in the correct position. The 1 under Cows is for the E, which is present in source word but is not in the correct position.
 
## The Program
Run try.py. Player one then types in the source word and presses enter. Player two then gets to guessing the word.

Have fun!
