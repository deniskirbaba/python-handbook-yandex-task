from itertools import product

expression = input()

v = sorted(list(set(expression.split()) - {'and', 'or', 'not'}))
combinations = product([0, 1], repeat=len(v))

print(' '.join(v + ['F']))
[print(f'{" ".join([str(i) for i in comb])} {int(eval(expression, {}, {var: int(val) for var, val in zip(v, comb)}))}')
 for comb in combinations]
