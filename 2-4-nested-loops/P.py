table_size = int(input())
column_width = int(input())

separator = '\n' + '-' * (table_size * column_width + table_size - 1) + '\n'
rows = []
for row in range(1, table_size + 1):
    values = []
    for column in range(1, table_size + 1):
        values.append(f'{row * column: ^{column_width}}')
    rows.append('|'.join(values))

print(separator.join(rows))