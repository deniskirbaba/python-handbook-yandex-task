from itertools import product

n_parts = int(input())
n_iter = range(1, n_parts - 1)

print('А Б В')
[print(f'{a} {b} {n_parts - a - b}') for a, b in product(n_iter, n_iter) if n_parts - a - b > 0]
