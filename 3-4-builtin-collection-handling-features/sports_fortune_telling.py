from itertools import permutations

n_athletes = int(input())

name_athletes = sorted(input() for i in range(n_athletes))
[print(', '.join(comb)) for comb in permutations(name_athletes, r=3)]
