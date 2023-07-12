left = 1
right = 1000
mid = (left + right) // 2

while left <= right:
    print(mid)
    response = input()
    if response == "Угадал!":
        break
    elif response == "Больше":
        left = mid + 1
    else:
        right = mid - 1
    mid = (left + right) // 2
