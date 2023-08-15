import math

n = int(input())

flag = True
if n == 1:
    flag = False

for i in range(2, round(n ** 0.5 + 1)):
    if (n % i) == 0:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')
