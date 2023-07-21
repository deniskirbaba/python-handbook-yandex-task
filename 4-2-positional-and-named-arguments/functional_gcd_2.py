from functools import reduce


def gcd_2(a, b):
    while (r := a % b) != 0:
        a = b
        b = r
    return b


def gcd(*args):
    if len(args) == 1:
        return args[0]
    res = args[0]
    for i in args[1:]:
        while (r := res % i) != 0:
            res = i
            i = r
        res = i
    return res

print(gcd(36, 48, 156, 100500))
