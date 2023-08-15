height = int(input())
width = int(input())

max_n = height * width

val = 1
for i in range(1, height + 1):
    for j in range(1, width + 1):
        print(str(val).rjust(len(str(max_n))), end=' ')
        val += 1
    print()