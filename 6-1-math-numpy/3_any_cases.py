from math import comb


n, m = [int(i) for i in input().split()]
print(comb(n - 1, m - 1), comb(n, m))
