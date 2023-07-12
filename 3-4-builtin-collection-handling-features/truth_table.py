from itertools import product

logic_function = input()

print('a b c f')
[print(f'{a} {b} {c} {int(eval(logic_function))}') for a, b, c in product([0, 1], [0, 1], [0, 1])]
