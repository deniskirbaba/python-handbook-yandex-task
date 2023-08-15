import math

orange = int(input())
res = 0
for i in range(orange):
    q = int(input())
    if q == 1:
        continue
    flag = True
    for j in range(2, round(q ** 0.5 + 1)):
        if (q % j) == 0:
            flag = False
            break
    if flag:
        res += 1
print(res)
