from itertools import product, combinations

cards_in_combination = 3

suit_present = input()
nominal_missing = input()
prev_comb = [comb.split() for comb in input().split(', ')]

suits = sorted(['пик', 'треф', 'бубен', 'червей'])
nominals = sorted(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'])

match suit_present:
    case 'пики':
        suit_present = 'пик'
    case 'трефы':
        suit_present = 'треф'
    case 'буби':
        suit_present = 'бубен'
    case 'черви':
        suit_present = 'червей'

nominals.remove(nominal_missing)

combinations_iter = (i for i in combinations(product(nominals, suits), r=cards_in_combination)
                     if suit_present in (j[1] for j in i))

while True:
    cur_comb = [[j for j in i] for i in next(combinations_iter)]
    if prev_comb == cur_comb:
        print(', '.join([' '.join(list(combination)) for combination in next(combinations_iter)]))
        break
