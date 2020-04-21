import getpass
import pandas
# import sys
# import msvcrt
#Take word input from user 1word

print("Give first word")
# root_word = input()
root_word = getpass.getpass("")
step_count = 0
print("Attempt starts")
col = ("Attempt word", "Cows", "Bulls")
score_keeper = pandas.DataFrame(columns=col)
# word = input()
#Cows mean correct letter, wrong place; bulls mean correct letter, correct place
length = len(root_word)
print("Length -", length)
counter = 0
while True:
    cows = 0
    bulls = 0
    # print("Attempt ", counter)
    word = input()
    i = 0
    while i < length:
        if root_word[i] == word[i]:
            bulls += 1
            # print(bulls)
        i += 1
    i = 0
    while i < length:
        if root_word[i] in word and root_word[i] != word[i]:
            # print("yo")
            cows += 1
            # print("Cows -", cows)
        i += 1
    # print("Cows - ", cows, "Bulls - ", bulls)
    score_keeper.loc[counter] = [word] + list((cows, bulls))
    print(score_keeper)
    if bulls == length and word == root_word:
        break
    counter += 1
