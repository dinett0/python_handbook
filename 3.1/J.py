whole = ""
while (word := input()) != "ФИНИШ":
    whole += word.lower()
alpha = {}
for charachter in whole.replace(" ", ""):
    alpha[charachter] = 0
for charachter in whole.replace(" ", ""):
    alpha[charachter] += 1
print(max(alpha, key=alpha.get))
