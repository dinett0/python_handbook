# a = int(input())
# b = int(input())

a = input()
b = input()
c = input()

smol = a if a < b else b
smol = c if c < smol else smol
print(smol)
