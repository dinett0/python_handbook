times = int(input())
whole_set = set()
for i in range(times):
    whole_set |= set(input().split())

for i in whole_set:
    print(i)
