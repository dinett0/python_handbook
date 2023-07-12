times = int(input()) - 1
max_name = input()
for k in range(times):
    max_name = min(max_name, input())
print(max_name)
