from itertools import product


# 1. input expr str -> list['str'] (vars and operators)
# using replace, iter (match)
# as well as form variable array
expr = input().replace(' ', '')
vars_ops_list = list()
vars_list = set()
idx = 0
while idx < len(expr):
    ch = expr[idx]
    if ch.isupper():
        vars_ops_list.append(ch)
        vars_list.add(ch)
    else:
        match ch:
            case 'n':
                vars_ops_list.append('not')
                idx += 2
            case 'a':
                vars_ops_list.append('and')
                idx += 2
            case 'o':
                vars_ops_list.append('or')
                idx += 1
            case '-':
                vars_ops_list.append('->')
                idx += 1
            case _:
                vars_ops_list.append(ch)
    idx += 1

vars_list = sorted(list(vars_list))

# print(vars_ops_list)
# print(vars_list)

# 2. convert to RPN
# using operators precedence and 2 strcutures (output queue and operators stack)
'''
RPN algorithm
1. always add vars to output_queue
2. push operator to operator_stack if: stack is empty or precedence leq precedence prev operator (in stack)
3. pop operator_stack and append to queue while precedence greater than precedence of last operator (in stack) 
   and push cur operator in op_stack
4. if end of expression then pop all values from stack to end of queue
5. '(' push to the operator_stack always
6. if ')' then pop all the operators from stack to the out_queue until '('
'''
output_q = list()
oper_st = list()
precedence = {'(': 0,
              'not': 1,
              'and': 2,
              'or': 3,
              '^': 4,
              '->': 5,
              '~': 6}
for token in vars_ops_list:
    if token.isupper():
        output_q.append(token)
    else:
        if not oper_st:
            oper_st.append(token)
        else:
            if token == ')':
                while oper_st[-1] != '(':
                    output_q.append(oper_st.pop())
                oper_st.pop()
            elif precedence[token] < precedence[oper_st[-1]]:
                oper_st.append(token)
            else:
                while oper_st and (precedence[token] >= precedence[oper_st[-1]]) and (oper_st[-1] != '('):
                    output_q.append(oper_st.pop())
                oper_st.append(token)
while oper_st:
    output_q.append(oper_st.pop())

# print(output_q)

# 3. evaluate expression in RPN form
# using match for selecting operations
'''
Evaluation algorithm
Moving in output_q, while meet operator< calculate operation on operands, remove operands, operator and add result

Create function to do this. Function takes expression in RPN form (list['str']) and dictionary with values of vars
'''


def evaluate_rpn(rpn_expr_list, value_dict):
    # change all symbolic vars to exact values
    for idx, token in enumerate(rpn_expr_list):
        if token in value_dict:
            rpn_expr_list[idx] = value_dict[token]
            
    idx = 0
    while len(rpn_expr_list) > 1:
        token = rpn_expr_list[idx]
        if isinstance(token, str):
            match token:
                case 'not':
                    rpn_expr_list[idx - 1] = not rpn_expr_list[idx - 1]
                    del rpn_expr_list[idx]
                case 'and':
                    rpn_expr_list[idx - 2] = rpn_expr_list[idx - 2] and rpn_expr_list[idx - 1]
                    del rpn_expr_list[idx - 1:idx + 1]
                    idx -= 1
                case 'or':
                    rpn_expr_list[idx - 2] = rpn_expr_list[idx - 2] or rpn_expr_list[idx - 1]
                    del rpn_expr_list[idx - 1:idx + 1]
                    idx -= 1
                case '^':
                    rpn_expr_list[idx - 2] = rpn_expr_list[idx - 2] != rpn_expr_list[idx - 1]
                    del rpn_expr_list[idx - 1:idx + 1]
                    idx -= 1
                case '->':
                    rpn_expr_list[idx - 2] = rpn_expr_list[idx - 2] <= rpn_expr_list[idx - 1]
                    del rpn_expr_list[idx - 1:idx + 1]
                    idx -= 1
                case '~':
                    rpn_expr_list[idx - 2] = rpn_expr_list[idx - 2] == rpn_expr_list[idx - 1]
                    del rpn_expr_list[idx - 1:idx + 1]
                    idx -= 1
        else:
            idx += 1
    return int(rpn_expr_list[0])


# print(evaluate_rpn(output_q.copy(), {'A': 1, 'B': 1, 'C': 0}))

# 4. create truth table and evaluate all combinations

logic_combs = product([0, 1], repeat=len(vars_list))

print(' '.join(vars_list + ['F']))
for comb in logic_combs:
    res = evaluate_rpn(output_q.copy(), {vars_list[j]: comb[j] for j in range(len(vars_list))})
    print(f'{" ".join([str(i) for i in comb])} {res}')
