n = input()

left_idx = 0
right_idx = len(n) - 1

pal_flag = True

while left_idx < right_idx:
    if n[left_idx] != n[right_idx]:
        pal_flag = False
        break
    left_idx += 1
    right_idx -= 1

if pal_flag:
    print('YES')
else:
    print('NO')