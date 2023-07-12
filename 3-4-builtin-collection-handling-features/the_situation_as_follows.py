from itertools import product, combinations

n_cards = 3
comb_shows = 10

suits = sorted(['пик', 'треф', 'бубен', 'червей'])
nominals = sorted(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'])

suit_present = input()
nominal_missing = input()

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

combinations_iter = (i for i in combinations(product(nominals, suits), r=n_cards) if suit_present in (j[1] for j in i))

for i in range(comb_shows):
    print(', '.join([' '.join(list(combination)) for combination in next(combinations_iter)]))
