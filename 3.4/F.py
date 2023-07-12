import itertools

suit = ['пик', 'треф', 'бубен', 'червей']
suit.remove(input())
denominations = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

for i, j in itertools.product(denominations, suit):
    print(i, j)
    