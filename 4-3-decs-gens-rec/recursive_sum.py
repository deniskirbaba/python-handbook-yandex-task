def recursive_sum(*args):
    global res
    if 'res' not in globals():
        res = 0

    if len(args) > 0:
        res += args[-1]
        return recursive_sum(*args[:-1])
    
    return res


result = recursive_sum(1, 2, 3, 4, 5, 6)
print(result)
