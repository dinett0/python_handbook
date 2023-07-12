times = int(input())
shared = set()
unique = set()
for i in range(times):
    A = set()
    for string in input().split(":")[1].split(","):
        A |= {string.strip()}
    A -= shared
    shared |= A & unique
    unique ^= A

for toy in sorted(unique):
    print(toy)
