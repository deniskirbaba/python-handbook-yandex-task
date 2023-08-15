from math import gcd

numbers = set([int(i) for i in input().split('; ')])

mutually_simple = dict()

for i in numbers:
    for j in (numbers - {i, }):
        if gcd(i, j) == 1:
            mutually_simple[i] = mutually_simple.get(i, []) + [j]

for i in sorted(list(mutually_simple.keys())):
    print(f'{i} - {", ".join([str(j) for j in sorted(list(mutually_simple[i]))])}')
