from itertools import product

suits = ['пик', 'треф', 'бубен', 'червей']
nominals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

discarded_suit = input()

suits.remove(discarded_suit)

[print(f'{nominal} {suit}') for nominal, suit in product(nominals, suits)]
