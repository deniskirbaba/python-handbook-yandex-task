from itertools import accumulate

s = input().split()
for i in range(len(s) - 1):
    s[i] += ' '

[print(i) for i in accumulate(s)]
