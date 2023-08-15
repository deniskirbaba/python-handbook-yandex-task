n = int(input())
res = 0
while n > 0:
	if (n % 10) > res:
		res = n % 10
	n = n // 10
print(res)
