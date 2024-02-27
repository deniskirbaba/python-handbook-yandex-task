height = int(input())
width = int(input())

max_value_width = len(str(height * width))

for i in range(height):
    if i % 2 == 0:
        print(' '.join([f'{j + i * width: >{max_value_width}}' for j in range(1, width + 1)]))
    else:
        print(' '.join([f'{j + i * width: >{max_value_width}}' for j in range(width, 0, -1)]))