line_1 = input().split(', ')
line_2 = input().split(', ')

[print(f'{from_line_1} - {from_line_2}') for from_line_1, from_line_2 in zip(line_1, line_2)]
