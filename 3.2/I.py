dict = {}
while (line := input()) != "":
    for word in line.split():
        dict[word] = dict.get(word, 0) + 1

for key, value in dict.items():
    print(key, value)
