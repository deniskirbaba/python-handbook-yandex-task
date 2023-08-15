import math

n = int(input())
res = ''
for i in range(n):
	cur_n = int(input())
	cur_max = 0
	while cur_n > 0:
		cur_d = cur_n % 10
		if cur_d > cur_max:
			cur_max = cur_d
		cur_n = cur_n // 10
	res += str(cur_max)

print(res)
