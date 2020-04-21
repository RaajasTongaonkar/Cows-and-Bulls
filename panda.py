import pandas

col = ("Attempt word", "Cows", "Bulls")
score = pandas.DataFrame(columns=col, dtype=int)
print(score)
score.loc[0] = ["Code"] + list((1, 2))
print(score)
score.loc[1] = ["Attempt"] + list((2, 2))
print(score)
