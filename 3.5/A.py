from sys import stdin

sum = 0
for x in stdin.read().split():
    sum += int(x)
print(sum)
