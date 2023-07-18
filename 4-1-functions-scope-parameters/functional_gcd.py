def gcd(a, b):
    while (r := (a % b)) != 0:
        a = b
        b = r
    return b

print(gcd(12, 45))
