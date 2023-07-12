n = int(input())
if n <= 1:
    print("NO")
else:
    prime = True
    for i in range(2, int(n**(1 / 2)) + 1):
        if n % i == 0:
            prime = False
    print("YES" if prime else "NO")
