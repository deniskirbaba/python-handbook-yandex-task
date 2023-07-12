from itertools import product

size = int(input())
numbers_iter = [i for i in range(1, size + 1)]

[print(' '.join([str(i * j) for i, j in product(numbers_iter, [k])])) for k in range(1, size + 1)]
