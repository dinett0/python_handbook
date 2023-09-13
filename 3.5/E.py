from sys import stdin

strings = stdin.read().split()
ans = set()
for string in strings:
    if string.lower() == string[::-1].lower():
        ans.add(string)

for string in sorted(ans):
    print(string)
