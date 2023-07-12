from itertools import chain, permutations

n_members = int(input())
n_available_products = 3

products = sorted(chain.from_iterable(((input().split(', ')) for i in range(n_members))))

[print(' '.join(prod)) for prod in permutations(products, r=n_available_products)]
