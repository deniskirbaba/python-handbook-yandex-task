n = int(input())
out = -1
blockchain = []

for i in range(n):
	blockchain.append(int(input()))

h_prev = 0
for i in range(n):
	h = blockchain[i] % 256
	if (i > 0) and (h >= 100):
		out = i
		break
	r = blockchain[i] // 256 % 256
	m = blockchain[i] // (256 ** 2)

	if (h != (37 * ((m + r + h_prev)) % 256)):
		out = i
		break

	h_prev = h

print(out)
