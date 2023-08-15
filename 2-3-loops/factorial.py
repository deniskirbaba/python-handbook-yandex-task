n = int(input())

if n == 0:
    print(1)
else:
    res = 1
    while n > 1:
        res *= n
        n -= 1
    print(res)
