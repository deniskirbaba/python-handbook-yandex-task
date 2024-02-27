height = int(input())
width = int(input())

max_value = height * width
w = len(str(max_value))

for i in range(1, height + 1):
    print(' '.join([f'{i + j * height: >{w}}' for j in range(width)]))
        