value = int(input())

d3 = value % 10
d2 = value // 10 % 10
d1 = value // 100

d_asc_sorted = sorted([d1, d2, d3])

max2d = d_asc_sorted[2] * 10 + d_asc_sorted[1]

if d_asc_sorted[0] == 0:
    if d_asc_sorted[1] == 0:
        min2d = d_asc_sorted[2] * 10
    else:
        min2d = d_asc_sorted[1] * 10
else:
    min2d = d_asc_sorted[0] * 10 + d_asc_sorted[1]

print(min2d, max2d)