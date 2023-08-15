import math

n = int(input())
best = 0
best_name = None
for i in range(n):
	cur_name = input()
	cur_n = int(input())
	cur_sum = 0
	while cur_n > 0:
		cur_sum += cur_n % 10
		cur_n = cur_n // 10
	if cur_sum >= best:
		best = cur_sum
		best_name = cur_name
print(best_name)
