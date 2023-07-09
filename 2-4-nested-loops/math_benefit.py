n = int(input())
digits = []
max_n_s = 11
max_sum_n_s = 0
for i in range(10, 1, -1):
    n_cur = n
    while n_cur > 0:
        digits.append(n_cur % i)
        n_cur = n_cur // i
    cur_sum = sum(digits)
    digits.clear()
    if cur_sum >= max_sum_n_s:
        max_n_s = i
        max_sum_n_s = cur_sum
print(max_n_s)