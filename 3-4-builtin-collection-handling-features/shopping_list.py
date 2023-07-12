from itertools import chain

products = chain.from_iterable([[i for i in input().split(', ')] for j in range(3)])

[print(f'{idx}. {position}') for idx, position in enumerate(sorted(list(products)), 1)]
