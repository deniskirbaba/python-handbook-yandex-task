from itertools import chain

n_members = int(input())

get_products = ((i for i in input().split(', ')) for j in range(n_members))

products = chain.from_iterable(get_products)

[print(f'{idx}. {position}') for idx, position in enumerate(sorted(list(products)), 1)]
