height = int(input())
width = int(input())

max_value = height * width
w = len(str(max_value))

for i in range(height):
    row = []
    for j in range(width):
        if j % 2 == 0:
            row.append(i + 1 + j * height)
        else:
            row.append((height - i) + j * height)
    print(' '.join([f'{str(i): >{w}}' for i in row]))