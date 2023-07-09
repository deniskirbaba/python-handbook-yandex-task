n = int(input())

cur_n = 1
n_str = 1
flag = True

while flag:
	for j in range(n_str):
		if cur_n > n:
			flag = False
			break
		if j != (n_str - 1):
			print(cur_n, end=' ')
		else:
			print(cur_n, end='\n')
		cur_n += 1
	n_str += 1
