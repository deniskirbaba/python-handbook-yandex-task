s = input()
cur_l = 1
cur_d = s[0]
for i, digit in enumerate(s[1:]):
    if digit == cur_d:
        cur_l += 1
        continue
    else:
        print(f'{cur_d} {cur_l}')
        cur_d = digit
        cur_l = 1
print(f'{cur_d} {cur_l}')
