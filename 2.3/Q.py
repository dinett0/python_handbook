a = int(input())
buff = ""
while a != 0:
    tmp = a % 10
    if tmp % 2 != 0:
        buff = str(tmp) + buff
    a //= 10
print(buff)
