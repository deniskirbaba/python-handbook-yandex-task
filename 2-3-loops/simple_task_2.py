import math

n = int(input())

primes = []
all_primes = [2]
cur_prime = 2

while n > 1:
	if (n % cur_prime) == 0:
		primes.append(cur_prime)
		n = n // cur_prime
		continue
	else:
		cur_prime += 1
		flag = True
		while flag:
			for idx, i in enumerate(all_primes):
				if (cur_prime % i) == 0:
					cur_prime += 1
					break
				elif idx == (len(all_primes) - 1):
					all_primes.append(cur_prime)
					flag = False
					break

out = ""
for i in range(len(primes) - 1):
	out += str(primes[i]) + ' * '
out += str(primes[-1])
print(out)
