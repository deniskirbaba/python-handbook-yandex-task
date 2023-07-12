from itertools import product


logic_expr = input()
logic_vars = sorted(list({symbol for symbol in logic_expr if symbol.isupper()}))
logic_combs = product([0, 1], repeat=len(logic_vars))
expr_mod = logic_expr.replace('~', '==').replace('->', '<=')

print(' '.join(logic_vars + ['F']))
[print(f'{" ".join([str(i) for i in comb])} {int(eval(expr_mod, {}, {var: int(val) for var, val in zip(logic_vars, comb)}))}')
 for comb in logic_combs]
