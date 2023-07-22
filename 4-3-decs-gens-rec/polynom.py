def make_equation(*args):
    global res
    if 'res' not in globals():
        if len(args) != 0:
            res = str(args[0])
            return make_equation(*args[1:])
        return ''
    
    if len(args) > 0:
        res = '(' + res + ') * x + ' + str(args[0])
        return make_equation(*args[1:])
    return res


result = make_equation(3, 1, 5, 3)
print(result)
