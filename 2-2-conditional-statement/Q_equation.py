import math

a = float(input())
b = float(input())
c = float(input())

if a == 0:
	if b == 0:
		if c == 0:
			print('Infinite solutions')
		else:
			print('No solution')
	else:
		print(round(-c / b, 2))
else:
	d = b**2 - 4 * a * c

	if d < 0:
		print('No solution')
	elif d == 0:
		print(round(-b / (2 * a), 2))
	else:
		q1 = (-b - math.sqrt(d)) / (2 * a)
		q2 = (-b + math.sqrt(d)) / (2 * a)
		q = [q1, q2]
		q.sort()
		print(f'{round(q[0], 2)} {round(q[1], 2)}')
