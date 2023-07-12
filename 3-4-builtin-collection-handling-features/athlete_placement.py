from itertools import permutations

n_athletes = int(input())

athletes_names = sorted(input() for i in range(n_athletes))
[print(', '.join(perm)) for perm in permutations(athletes_names)]
